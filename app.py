from flask import Flask, redirect, url_for, Blueprint
from Module.Login.loginControllers.loginController import login_bp
from Module.Index.indexController.IndexController import index_bp
import requests

app = Flask(__name__)

app.register_blueprint(login_bp)
app.register_blueprint(index_bp)

app.secret_key = 'normalmotora'

@app.route('/')
def login():
    return redirect(url_for('login_bp.login'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)