from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

credentials = ""
print(credentials)

@app.route('/estado_boton', methods=['POST'])
def received():
    global credentials
    try:
        data = request.get_json(force=True)
        if 'credenciales' in data:
            credentials = data['credenciales']
            print("Credenciales recibidas:", credentials)
            return jsonify({
                "mensaje": "Credenciales recibidas", 
                "credenciales": credentials
            }), 200
        else:
            return jsonify({"error": "No se enviaron credenciales"}), 400
    except Exception as e:
        return jsonify({"error": f"Error al procesar: {str(e)}"}), 400

@app.route('/get_credentials', methods=['GET'])
def get_credentials():
    global credentials
    respuesta = credentials
    credentials = ""  # Limpiar las credenciales despues de enviarlas
    return jsonify({"credenciales": respuesta})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
