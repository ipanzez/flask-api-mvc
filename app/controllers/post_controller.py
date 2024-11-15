from app.models.post import Post
from app import db

def get_all_posts():
    posts = Post.query.all()
    return [post.to_dict() for post in posts]

def create_post(data):
    post = Post(
        title=data.get('title'),
        content=data.get('content'),
        user_id=data.get('user_id')
    )
    db.session.add(post)
    db.session.commit()
    return post.to_dict()

def get_post_by_id(post_id):
    post = Post.query.get(post_id)
    if post:
        return post.to_dict()
    return None
