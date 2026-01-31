from flask import Blueprint, request, jsonify
from app.users import register_user, login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user, error = register_user(data["username"], data["password"])

    if error:
        return jsonify({"error": error}), 400

    return jsonify({"message": "User registered", "user": user}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    session_key = login_user(data["username"], data["password"])

    if not session_key:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"session_key": session_key})
