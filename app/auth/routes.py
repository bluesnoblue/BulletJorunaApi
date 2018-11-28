from app import db
from app.auth import bp
from flask_jwt import jwt_required,current_identity
from flask import jsonify,abort,request
from app.models import User


@bp.route('/users', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        print('test1')
        abort(400)
    if User.query.filter_by(username=username).first() is not None:
        print(User.query.filter_by(username=username).first())
        abort(400)
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

