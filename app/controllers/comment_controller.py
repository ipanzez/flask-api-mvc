from app.models.comment import Comment
from app import db

def get_all_comments():
    comments = Comment.query.all()
    return [comment.to_dict() for comment in comments]

def create_comment(data):
    comment = Comment(
        content=data.get('content'),
        user_id=data.get('user_id'),
        post_id=data.get('post_id')
    )
    db.session.add(comment)
    db.session.commit()
    return comment.to_dict()

def get_comment_by_id(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        return comment.to_dict()
    return None
