from flask import Blueprint, request, jsonify
from app.controllers.comment_controller import get_all_comments, create_comment, get_comment_by_id

comment_bp = Blueprint('comment', __name__, url_prefix='/api/comments')

@comment_bp.route('/', methods=['GET'])
def list_comments():
    comments = get_all_comments()
    return jsonify(comments), 200

@comment_bp.route('/', methods=['POST'])
def add_comment():
    data = request.get_json()
    new_comment = create_comment(data)
    return jsonify(new_comment), 201

@comment_bp.route('/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = get_comment_by_id(comment_id)
    if comment:
        return jsonify(comment), 200
    return jsonify({"message": "Comment not found"}), 404
