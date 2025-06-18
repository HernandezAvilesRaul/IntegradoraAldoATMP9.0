from flask import Flask, render_template, request, redirect, url_for, session
from Module.Login.loginControllers.loginController import login_bp

app = Flask(__name__)
app.register_blueprint(login_bp)
app.secret_key = 'normalmotora'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)