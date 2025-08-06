from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # Necesario para Flask-SocketIO
socketio = SocketIO(app)

# Diccionario para almacenar los datos más recientes de cada dispositivo
latest_data = {}

# Función para obtener la lista de dispositivos (debes adaptarla a tu base de datos)
def get_devices():
    return ['dispositivo1','dispositivo2','dispositivo13' ,'dispositivo4']

@app.route('/index')
def index():
    devices = get_devices()
    print(devices, "Fornite devices data")
    return render_template('index.html', devices=devices)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print("Datos recibidos:", data)  
    device_name = data.get('device_name')
    if device_name:
        latest_data[device_name] = data
        socketio.emit('update', data, room=device_name)
        return 'Datos recibidos', 200
    else:
        return 'Falta device_name', 400
    
@socketio.on('join')
def on_join(data):
    device_name = data['device_name']
    join_room(device_name)
    if device_name in latest_data:
        socketio.emit('update', latest_data[device_name], room=request.sid)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')