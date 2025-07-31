from flask import Blueprint, redirect, render_template, request, url_for, jsonify
from ..loginConstants.loginLogic import saved_keys
import json


login_bp = Blueprint("login_bp", __name__, 
                     template_folder="../../../Model/Login/loginViews", 
                     static_folder="../../../Model/Login/loginStyles")

@login_bp.route("/received_keys", methods=['POST', 'GET'])
def received_crendetials():
    if request.method == "POST":
        try:
            file = request.files["license"]
        
            content = json.load(file)
            username = content["user"]
            key = content["key_code"]

            
        except Exception as e:
            print(f"Error: {e}")

    return redirect(url_for("login"))

@login_bp.route('/login')
def login():
    return render_template('login.html')
