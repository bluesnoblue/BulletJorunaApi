from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.auth.auth import authenticate, identity
    jwt = JWT(app, authenticate, identity)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    from app.bullet import bp as bullet_bp
    app.register_blueprint(bullet_bp)

    return app
from app import models
