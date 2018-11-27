from app import db
from app.user import bp
from app.models import User,Token
from flask import request, abort, jsonify, url_for
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@bp.route('/users', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username=username).first() is not None:
        abort(400)
    user = User(username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201


@bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        abort(400)
    token = Token(user.get_token(), user.id)
    db.session.add(token)
    db.session.commit()
    return jsonify({'user': user.id, 'token': token.token}), 201


@bp.route('/user', methods=['GET'])
def profile():
    authorization = request.headers.get('authorization')
    if authorization and authorization.split()[0] == 'bearer':
        user = User.verify_token(authorization.split()[1])
        if user:
            return jsonify({'id': user.id, 'name': user.username, 'email': user.email, 'mobile': user.mobile}), 201
    return jsonify({'message': 'error'})







