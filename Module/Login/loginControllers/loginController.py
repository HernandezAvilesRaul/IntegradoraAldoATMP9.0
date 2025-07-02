from flask import Blueprint, redirect, render_template, request, url_for, jsonify
from ..loginConstants.loginLogic import authenticateCredentials
login_bp = Blueprint("login_bp", __name__, 
                     template_folder="../../../Model/Login/loginViews", 
                     static_folder="../../../Model/Login/loginStyles")

credentials = ""

@login_bp.route("/receivedCredentials", methods=['POST'])
def receivedCredentials():
    global credentials
    global user
    global password
    try:
        data = request.get_json(force=True)
        if 'credenciales' in data:
            credentials = data['credenciales']
            user = credentials.get('user')
            password = credentials.get('password')
            print("Credenciales recibidas:", credentials)

            username = authenticateCredentials(user, password)
            
            if username:  # Si authenticateCredentials devuelve un username (no None)
                return jsonify({
                    "success": True,
                    "username": username,
                    "redirect": url_for('index_bp.index')  # Genera la URL '/index'
                })
            else:
                return jsonify({
                    "success": False,
                    "message": "Credenciales inválidas"
                })
        else:
            return jsonify({"error": "No se enviaron credenciales"}), 400
    except Exception as e:
        return jsonify({"error": f"Error al procesar: {str(e)}"}), 400

@login_bp.route('/get_credentials', methods=['GET'])
def get_credentials():
    global credentials
    respuesta = credentials
    credentials = ""  # Limpiar las credenciales después de enviarlas
    return jsonify({"credenciales": respuesta})

@login_bp.route('/test_db_users')
def test_db_users():
    respuesta = authenticateCredentials(user, password)
    return jsonify(respuesta)

@login_bp.route('/login')
def login():
    return render_template('login.html')
