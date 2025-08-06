from .db import get_db_connection
import mysql.connector

def saved_keys(username, key):
    try:
        cnx = get_db_connection()
        cur = cnx.cursor()
        args = [username, key, False]

        cur.callproc('verify_keys', args)

        output_args = cur.callproc('verify_keys', args)

        print("Resultado:", output_args[2])
        
        if output_args[2] == True:
            cnx.close()
            cur.close()

            return output_args[2]  

        else:
            return "Invalid Credentials"

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
