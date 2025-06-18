from flask import Blueprint, redirect, render_template, request, url_for
from ..loginConstants.loginLogic import authenticateCredentials

login_bp = Blueprint("login_bp", __name__, 
                     template_folder="../loginViews", 
                     static_folder="../loginStyles/")

@login_bp.route("/", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if authenticateCredentials(username, password):
            return 'it worked'
        else:
            return 'KYS'

    return render_template("login.html")

