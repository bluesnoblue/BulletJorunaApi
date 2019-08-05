from app.models import User
from flask import abort


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        abort(403)
    return user


def identity(payload):
    user_id = payload['identity']
    user = User.query.filter_by(id=user_id).first()
    return user
