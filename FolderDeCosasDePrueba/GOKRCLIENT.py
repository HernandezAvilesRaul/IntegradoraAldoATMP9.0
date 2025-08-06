import requests
import time
import random

SERVER_URL = "http://192.168.100.41:5000/data"

def send_sensor_data(device_name):
    while True:
        data = {
            "device_name": device_name,
            "temperatura": round(random.uniform(20.0, 30.0), 2),
            "humedad": random.randint(40, 80),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            response = requests.post(SERVER_URL, json=data)
            print(f"Datos enviados: {data} | Respuesta: {response.text}")
        except Exception as e:
            print(f"Error al enviar datos: {e}")

        time.sleep(5)
        
if __name__ == "__main__":
    send_sensor_data("dispositivo1")  # Cambia el nombre si necesitas