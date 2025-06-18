from flask import Blueprint, redirect, render_template, request

login_bp = Blueprint("login_bp", __name__, 
                     template_folder="../loginViews", 
                     static_folder="../loginStyles/")

@login_bp.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Form submitted"
    return render_template("login.html")

