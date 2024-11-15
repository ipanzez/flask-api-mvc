from flask import Blueprint, request, jsonify
from app.controllers.user_controller import get_all_users, create_user, get_user_by_id

user_bp = Blueprint('user', __name__, url_prefix='/api/users')

@user_bp.route('/', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify(users), 200

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = create_user(data)
    return jsonify(new_user), 201

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404
