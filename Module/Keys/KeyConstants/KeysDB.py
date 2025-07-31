from .db import get_db_connection
import mysql.connector
from argon2 import PasswordHasher
import string
import secrets

def save_key(username, hashed_key):
    try:
        cnx = get_db_connection()
        cur = cnx.cursor()

        cur.callproc('insert_keys', [username, hashed_key])
        cnx.commit()

        cnx.close()
        cur.close()
    except mysql.connector.Error as e:
        print(f"Error: {e}")

def generate_secret():
    alphabet = string.ascii_letters + string.digits
    secret = ''.join(secrets.choice(alphabet) for i in range(8))
    
    ph = PasswordHasher()
    hash = ph.hash(secret)
    return hash