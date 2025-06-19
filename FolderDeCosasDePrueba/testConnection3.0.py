from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

estado_boton = "UNKNOWN"
credentials = ""

@app.route('/estado_boton', methods=['GET','POST'])
def recibir_estado():
    global estado_boton
    data = request.get_json()
    if 'estado' in data:
        estado_boton = data['estado']
        return jsonify({"mensaje": "Estado recibido", "estado": estado_boton}), 200
    return jsonify({"error": "Formato incorrecto"}), 400

@app.route('/get_estado')
def get_estado():
    return jsonify({"estado": estado_boton})

@app.route('/get_credentials')
def get_credentials():
    return jsonify({"estado": credentials})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
