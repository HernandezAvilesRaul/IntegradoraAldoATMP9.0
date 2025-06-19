from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

estado_actual = "LOW"

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    socketio.emit('estado_actual', {'estado': estado_actual})

@app.route('/estado_boton', methods=['POST', 'GET'])
def recibir_estado():
    global estado_actual
    data = request.get_json()
    estado_actual = data.get('estado')
    socketio.emit('estado_actual', {'estado': estado_actual})  # Envía a todos los clientes
    return jsonify({'mensaje': 'Estado actualizado'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

    