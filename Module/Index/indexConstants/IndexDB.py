from .db import get_db_connection
import mysql.connector

def save_device(device, device_type, url):
    try:
        cnx = get_db_connection()
        cur = cnx.cursor()
        cur.callproc('sp_add_device', [device, device_type, url])
        cnx.commit()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        raise  # Propagar el error para manejarlo en el controlador
    finally:
        cur.close()
        cnx.close()

def read_devices():
    try:
        cnx = get_db_connection()
        cur = cnx.cursor()
        cur.callproc('ps_show_devices')
        devices_data = []
        for result in cur.stored_results():
            devices_data = result.fetchall()
        print("Datos de dispositivos:", devices_data)
        return devices_data
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        cur.close()
        cnx.close()