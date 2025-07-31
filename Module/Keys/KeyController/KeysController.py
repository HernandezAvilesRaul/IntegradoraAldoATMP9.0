from flask import Blueprint, render_template, request, send_file
from ..KeyConstants.KeysDB import save_key, generate_secret
import io
import json

keys_bp = Blueprint("keys_bp", __name__, 
                     template_folder="../../../Model/Keys/KeysViews", 
                     static_folder="../../../Model/Keys/KeysStyles")

@keys_bp.route('/key_generator', methods=["GET"])
def key_generator():
    return render_template('keys.html')

@keys_bp.route('/generate_key', methods=["POST"])
def generate_key():
    user_name = request.form.get("KeyUser")
    secret = generate_secret()
    
    key_content = {
        "user": user_name,
        "key_code": secret
    }
    save_key(user_name, secret)
    json_content = json.dumps(key_content, indent=4)

    # Crear archivo 
    file = io.BytesIO(json_content.encode("utf-8"))
    file.seek(0)

    return send_file(
        file,
        as_attachment=True,
        download_name=f"{user_name}'s_license.key",
        mimetype="text/plain"
    )






