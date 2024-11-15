from app.models.user import User
from app import db

def get_all_users():
    users = User.query.all()
    return [user.to_dict() for user in users]

def create_user(data):
    user = User(
        username=data.get('username'),
        email=data.get('email'),
        password=data.get('password')  # Password hashing diperlukan untuk keamanan
    )
    db.session.add(user)
    db.session.commit()
    return user.to_dict()

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return user.to_dict()
    return None
