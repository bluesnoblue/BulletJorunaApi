from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT
from flask_restful import Api
from flask_admin import Admin
from flask_login import LoginManager
from app.admin.views import AdminUserView,UserView,MyView

from config import Config

db = SQLAlchemy()
migrate = Migrate()
api = Api()

admin = Admin(name='后台管理系统',template_mode='bootstrap3')
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    login.init_app(app)

    from app.auth.auth import authenticate, identity
    jwt = JWT(app, authenticate, identity)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    from app.bullet import bp as bullet_bp
    app.register_blueprint(bullet_bp)

    from app.resource.routes import ResourcesTest, ResourceTest
    api.add_resource(ResourcesTest, '/resources')
    api.add_resource(ResourceTest, '/resource/<resource_id>')

    from app.resource import bp as res_bp
    api.init_app(res_bp)
    app.register_blueprint(res_bp)

    return app

from app import models

admin.add_view(MyView(name='页面1',category = '菜单项目'))
admin.add_view(UserView(models.User, db.session, name='用户列表',category = '用户管理'))
admin.add_view(AdminUserView(models.AdminUser, db.session, name='管理员'))