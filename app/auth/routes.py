from app import db
from app.auth import bp
from flask_jwt import jwt_required,current_identity
from flask import jsonify,request
from app.models import User


@bp.route('/users', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        return jsonify({'error': '请输入用户名和密码'}), 499
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': '用户已注册'}) , 499
    user = User(username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201

@bp.route('/user', methods=['GET'])
@jwt_required()
def current_user():
    return jsonify({
        'id': current_identity.id,
        'name': current_identity.username,
        'email': current_identity.email,
        'mobile': current_identity.mobile
    }), 201

