from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import pymysql
pymysql.install_as_MySQLdb()

# Inisialisasi Database dan Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Konfigurasi Database
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://testing_seenasage:c9494a8fc703a0cff94775cc547693ab8da2f6d2@vyxdh.h.filess.io:3307/testing_seenasage"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inisialisasi Extension
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register Blueprints
    from app.routes import init_routes
    init_routes(app)
    
    return app
