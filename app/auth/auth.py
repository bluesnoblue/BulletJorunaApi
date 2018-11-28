from app.models import User
from flask import abort, jsonify


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        abort(jsonify({'error': '用户名或密码有误'}))
    return user


def identity(payload):
    user_id = payload['identity']
    user = User.query.filter_by(id=user_id).first()
    return user
