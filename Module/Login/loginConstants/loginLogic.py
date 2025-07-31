from .db import get_db_connection
import mysql.connector

def saved_keys(key):
    try:
        args = []
        cnx = get_db_connection()
        cur = cnx.cursor()

        cur.callproc('verified_license', args)

        if len(args) > 0:
            cnx.close()
            cur.close()
            return args[0]
        else:
            cnx.close()
            cur.close()
            return "Invalid Credentials"
        
    except mysql.connector.Error as e:
        print(f"Error: {e}")

