from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_socketio import SocketIO, join_room
from ..indexConstants.IndexDB import save_device, read_devices
from Module.Decorators.Sessions import license_verification
from sockets import socketio
import requests

index_bp = Blueprint("index_bp", __name__, 
                     template_folder="../../../Model/Index/IndexViews", 
                     static_folder="../../../Model/Index/IndexStyles")


latest_data = {}

@index_bp.route("/register_device", methods=['POST'])
def register_device():
    device_name = request.form.get('device_name')
    device_type = request.form.get('device_type')
    device_url = request.form.get('device_url')
    
    if not all([device_name, device_type, device_url]):
        return jsonify({"error": "Faltan parámetros"}), 400
    
    try:
        save_device(device_name, device_type, device_url)
        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@index_bp.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print("Datos recibidos:", data)
    device_name = data.get('device_name')
    
    if not device_name:
        return jsonify({"error": "Falta device_name"}), 400
    
    latest_data[device_name] = {k: v for k, v in data.items() if k != 'device_name'}
   
    socketio.emit('update', {'device_name': device_name, **latest_data[device_name]}, room=device_name)
    return jsonify({"message": "Datos recibidos"}), 200

@socketio.on('join')
def on_join(data):
    device_name = data.get('device_name')
    print(f"[JOIN] Cliente {request.sid} quiere unirse a: {device_name}")
    if not device_name:
        return
    
    join_room(device_name)

    if device_name in latest_data:
        print(f"[EMIT] Enviando datos actuales a {request.sid}")
        socketio.emit('update', {'device_name': device_name,**latest_data[device_name]}, room=device_name)

@index_bp.route('/index', methods=['GET'])
@license_verification
def index():
    devices_info = read_devices()
    
    devices = [device[1] for device in devices_info if len(device) > 1]
    print("Dispositivos:", devices)
    return render_template('index.html', devices=devices)

@index_bp.route('/add_device', methods=['GET'])
def add_device():
    return render_template("register_devices.html")

@index_bp.route('/monitor_pc', methods=['GET'])
@license_verification
def monitor_pc():
    devices_info = read_devices()
    pc_devices = [d[1] for d in devices_info if d[2] == 'pc']
    return render_template('monitor_pc.html', devices=pc_devices)
