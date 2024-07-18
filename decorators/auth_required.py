from functools import wraps
from flask import session, jsonify

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'user_id' in session:
            return jsonify({
              'message': 'Brak uprawnień. Zaloguj się'
            })
        return f(*args, **kwargs)
        
    return decorated_function