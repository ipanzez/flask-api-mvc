from flask import Blueprint, request, jsonify
from app.controllers.post_controller import get_all_posts, create_post, get_post_by_id

post_bp = Blueprint('post', __name__, url_prefix='/api/posts')

@post_bp.route('/', methods=['GET'])
def list_posts():
    posts = get_all_posts()
    return jsonify(posts), 200

@post_bp.route('/', methods=['POST'])
def add_post():
    data = request.get_json()
    new_post = create_post(data)
    return jsonify(new_post), 201

@post_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = get_post_by_id(post_id)
    if post:
        return jsonify(post), 200
    return jsonify({"message": "Post not found"}), 404
