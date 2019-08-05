from app import db
from app.auth import bp
from app.models import User
from flask import request, jsonify
from flask_jwt import jwt_required, current_identity


@bp.route('/users', methods=['POST'])
def register():
    values = request.get_json()
    required = ['username', 'password']
    if not all(k in values for k in required):
        return jsonify({'error': '请输入用户名和密码'}), 499
    username = values['username']
    password = values['password']

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': '用户已注册'}), 499

    user = User(username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'username': user.username}), 201


@bp.route('/user', methods=['GET'])
@jwt_required()
def get_profile():
    return jsonify({
        'id': current_identity.id,
        'name': current_identity.username,
        'email': current_identity.email,
        'mobile': current_identity.mobile
    }), 201
