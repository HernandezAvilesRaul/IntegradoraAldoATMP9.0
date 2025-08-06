from flask import Blueprint, redirect, render_template, request, url_for, jsonify, session
from ..loginConstants.loginLogic import saved_keys
import json


login_bp = Blueprint("login_bp", __name__, 
                     template_folder="../../../Model/Login/loginViews", 
                     static_folder="../../../Model/Login/loginStyles")

@login_bp.route("/received_credentials", methods=['POST', 'GET'])
def received_credentials():
    if request.method == "POST":
        try:
            file = request.files["license"]
            content = json.load(file)
            session['username'] = content["user"]
            key = content["key_code"]
            response = saved_keys(session['username'], key)
            
            if response == 1:
                return jsonify({'status': 'success', 'redirect_url': url_for('index_bp.index')})  
            
            else :
                return jsonify({'status': 'error', 'message': 'Credenciales no validas'}), 401
            
        except Exception as e:
            return jsonify({'status': 'error', 'message': e}), 500
        

@login_bp.route('/login')
def login():
    session.clear()
    session.modified = True
    return render_template('login.html')

@login_bp.route('/logout', methods=["POST"])
def logout():
    session.clear()
    session.modified = True
    return redirect(url_for('login_bp.login'))