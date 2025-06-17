from flask import Flask, render_template, request, redirect, url_for, session
from Module.Login.loginController.loginLogic import authenticateCredentials


app = Flask(__name__, 
            template_folder="Module/Login/loginViews/",
            static_folder="Module/Login/loginStyles/")

app.secret_key = 'normalmotora'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if authenticateCredentials(username, password):
            session['user'] = username
            return redirect(url_for("index"))
        else:
            return render_template("badCredentials.html")
    
    return render_template("login.html")

@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template("../Module/Index/indexViews/index.html")

if __name__ == '__main__':
    app.run(debug=True)