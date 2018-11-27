from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    mobile = db.Column(db.String(11), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,username):
        self.username=username

    def __repr__(self):
        return '<User %s>' % self.username

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(), index=True, unique=True)
    created_time = db.Column()
# class Bullet(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.Integer)
#     status = db.Column(db.Integer)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True)
#     mark = db.Column(db.Integer)
#     user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
