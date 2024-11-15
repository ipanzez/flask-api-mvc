from app.routes.user_routes import user_bp
from app.routes.post_routes import post_bp
from app.routes.comment_routes import comment_bp

def init_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(comment_bp)
