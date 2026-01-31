from flask import request, jsonify
from functools import wraps
from app.users import verify_session

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        session_key = request.headers.get("Session-Key")
        if not session_key:
            return jsonify({"error": "Session key missing"}), 401

        session = verify_session(session_key)
        if not session:
            return jsonify({"error": "Invalid or expired session"}), 403

        return f(*args, **kwargs)
    return wrapper
