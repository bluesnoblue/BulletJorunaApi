from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    mobile = db.Column(db.String(11), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %s>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Bullet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bullet_type = db.Column(db.Integer)  # 任务 1事件 2记录
    status = db.Column(db.Integer, default=0)  # 0未完成 1已完成 2延后
    body = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, index=True)
    mark = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, bullet_type, body, user_id):
        self.status = 0
        self.bullet_type = bullet_type
        self.body = body
        self.user_id = user_id

    def __repr__(self):
        return '<Bullet %s form user_%s>' % (self.body, self.user_id)

    def update_mark(self):
        self.mark = (self.mark + 1) % 3

    def update_body(self):
        self.body = (self.mark + 1) % 3

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

