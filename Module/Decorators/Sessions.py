from functools import wraps
from flask import session, redirect, url_for, flash

def license_verification(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            flash("There are no session credentials")
            return redirect(url_for('login_bp.login'))
        return func(*args, **kwargs)
    return wrapper
