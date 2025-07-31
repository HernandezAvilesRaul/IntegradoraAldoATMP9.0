from flask import Flask, redirect, url_for, Blueprint
from Module.Login.loginControllers.loginController import login_bp
from Module.Index.indexController.IndexController import index_bp
from Module.Keys.KeyController.KeysController import keys_bp
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"

load_dotenv(dotenv_path=env_path)

if not os.getenv("secret_key"):
    print("No se pudo cargar el archivo .env o falta secret_key")


app = Flask(__name__)

app.register_blueprint(login_bp)
app.register_blueprint(index_bp)
app.register_blueprint(keys_bp)

app.secret_key = os.getenv('secret_key')

@app.route('/')
def login():
    return redirect(url_for('login_bp.login'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)
