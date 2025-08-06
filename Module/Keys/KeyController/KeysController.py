from flask import Blueprint, render_template, request, send_file, redirect, url_for
from ..KeyConstants.KeysDB import save_key, generate_secret, read_users, delete_key
from Module.Decorators.Sessions import license_verification
import io
import json

keys_bp = Blueprint("keys_bp", __name__, 
                     template_folder="../../../Model/Keys/KeysViews", 
                     static_folder="../../../Model/Keys/KeysStyles")

@keys_bp.route('/key_generator', methods=["GET"])
@license_verification
def key_generator():
    return render_template('keys.html')

@keys_bp.route('/generate_key', methods=["POST"])
def generate_key():
    username = request.form.get("KeyUser")
    secret = generate_secret()
    
    key_content = {
        "user": username,
        "key_code": secret
    }
    
    save_key(username, secret)
    json_content = json.dumps(key_content, indent=4)

    # Crear archivo 
    file = io.BytesIO(json_content.encode("utf-8"))
    file.seek(0)

    return send_file(
        file,
        as_attachment=True,
        download_name=f"{username}'s_license.key",
        mimetype="text/plain"
    )

@keys_bp.route('/show_keys', methods=['GET'])
@license_verification
def show_keys():
    results = read_users()
    return render_template('show_keys.html', users = results)

@keys_bp.route('/delete_keys/<int:id>/<username>', methods=['POST'])
@license_verification
def delete_keys(id, username):
    delete_key(id, username)
    return '', 204






