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

        cur.close()
        cnx.close()
        
    except mysql.connector.Error as e:
        print(f"Error: {e}")

def generate_secret():
    alphabet = string.ascii_letters + string.digits
    secret = ''.join(secrets.choice(alphabet) for i in range(8))
    
    ph = PasswordHasher()
    hash = ph.hash(secret)
    return hash

def read_users():
    try:
        user_data = []
        cnx = get_db_connection()
        cur = cnx.cursor()

        cur.callproc('sp_show_keys')
        
        for result in cur.stored_results():
            user_data = {row[1]: row[0] for row in result.fetchall()} 
                
        cur.close()
        cnx.close()
        return user_data
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        cur.close()
        cnx.close()

def delete_key(id, username):
    try:
        
        cnx = get_db_connection()
        cur = cnx.cursor()

        cur.callproc('sp_delete_key', [id, username])
        cnx.commit()

        cur.close()
        cnx.close()
        
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    return