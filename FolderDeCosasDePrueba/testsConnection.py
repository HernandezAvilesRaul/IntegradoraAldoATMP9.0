from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
estado_boton = "UNKNOWN"

@app.route('/estado_boton', methods=['POST'])
def recibir_estado():
    global estado_boton
    data = request.get_json()
    estado_boton = data.get("estado", "UNKNOWN")
    print(f"Botón: {estado_boton}")
    return jsonify({"mensaje": "Recibido"})

@app.route('/')
def pagina():
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head><title>Estado del Botón</title></head>
        <body>
            <h1>Estado del Botón (ESP32)</h1>
            <p id="estado">Cargando...</p>
            <script>
              setInterval(async () => {
                const res = await fetch("/estado_actual");
                const data = await res.json();
                document.getElementById("estado").textContent = data.estado;
              }, 1000);
            </script>
        </body>
        </html>
    """)

@app.route('/estado_actual')
def estado_actual():
    return jsonify({"estado": estado_boton})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
