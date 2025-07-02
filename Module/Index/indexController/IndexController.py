from flask import Blueprint, render_template, request
import requests

index_bp = Blueprint("index_bp", __name__, 
                     template_folder="../../../Model/Index/IndexViews", 
                     static_folder="../../../Model/Index/IndexStyles")

pcs = {
    "Laptop": "http://192.168.100.44:5001/metrics",
}

@index_bp.route("/pc/<name>")
def show_pc(name):
    url = pcs.get(name)
    if not url:
        return f"No se encontró la PC {name}", 404
    try:
        data = requests.get(url).json()
        return render_template("pcDetails.html", name=name, data=data)
    except Exception as e:
        return f"Error al obtener datos de {name}: {e}", 500

@index_bp.route('/index')
def index():
    return render_template('index.html',  pcs=pcs)