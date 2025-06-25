from .db import get_db_connection

get_db_connection()

def authenticateCredentials(user, password):
    args = [user, password, '', '', '']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    resultado = cursor.callproc('ValidateCredentials', args)

    encontrado = resultado[2]
    respuesta = resultado[3]
    username = resultado[4]

    print(f'Se encontro el el userID:"{encontrado}", Mensaje de respuesta"{respuesta}"')

    cursor.close()
    conn.close()

    return username
