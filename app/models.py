from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class AdminUser(db.Model, UserMixin):
    __tablename__ = 'admin_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=True, unique=True)
    account = db.Column(db.String(16), index=True, unique=True)
    description = db.Column(db.String(120), index=True, unique=True)
    password_hash  = db.Column(db.String(128))
    created_at = db.Column(db.DateTime,default=datetime.now)

    def __init__(self, username, account, password):
        self.username = username
        self.account = account
        self.set_password(password)

    def __repr__(self):
        return '<AdminUser %s>' % self.account

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    mobile = db.Column(db.String(11), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # role = db.relationship('roles', backref='user')

    def __init__(self, username,**kwargs):
        self.username = username
        # self.role = kwargs['role_id']
        # if self.role is None:
        #     self.role = Role.query.filter_by(default=True).first()

    def __repr__(self):
        return '<User %s>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self,permissions):
        return self.role is None and (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTRATOR)


class Bullet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True)
    bullet_type = db.Column(db.Integer)  # 任务 1事件 2记录
    status = db.Column(db.Integer, default=0)  # 0未完成 1已完成 2已取消 3已推迟
    content = db.Column(db.String(32))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, bullet_type, content, user_id, timestamp):
        self.status = 0
        self.bullet_type = bullet_type
        self.content = content
        self.user_id = user_id
        self.timestamp = timestamp

    def __repr__(self):
        return '<Bullet %s form user_%s>' % (self.body, self.user_id)

    def update_body(self, content):
        self.content = content

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def reopen(self):
        pass

    def cancel(self):
        pass

    def delay(self):
        pass


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(32))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True,nullable=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    permission = db.relationship('Permission', secondary='role_permission', backref='Role')

    def __repr__(self):
        return '<Role %s>'%self.name

    def __init__(self,name):
        self.name=name


class RolePermissons(db.Model):
    __tablename__ = 'role_permission'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'))


class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey("permissions.id"))

    def __repr__(self):
        return '<Permission %s>' % self.name

    def __init__(self,name,parent_id=None):
        self.name=name
        self.parent_id=parent_id