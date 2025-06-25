from dotenv import load_dotenv
import os
from pathlib import Path
import mysql.connector

# Obtener la ruta absoluta del archivo .env
env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

if not os.getenv("MYSQL_HOST"):
    print("No se pudo cargar el archivo .env o falta MYSQL_HOST")

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DB'),
        port=int(os.getenv('MYSQL_PORT', '3306'))
        )
    return conn
