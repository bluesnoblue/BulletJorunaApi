from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask import current_app
from time import time


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
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

    def get_token(self, expires_in=600):
        payload = {'user_id': self.id, 'exp': time() + expires_in}
        return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_token(token):
        try:
            print(token)
            user_id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithm=['HS256'])['user_id']
        except:
            return
        return User.query.filter_by(id=user_id).first()


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(), index=True, unique=True)
    created_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

# class Bullet(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.Integer)
#     status = db.Column(db.Integer)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True)
#     mark = db.Column(db.Integer)
#     user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
