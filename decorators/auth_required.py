from functools import wraps
from flask import session, jsonify, render_template

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'user_id' in session:
            return render_template('unauthorized.html')
        return f(*args, **kwargs)
        
    return decorated_function