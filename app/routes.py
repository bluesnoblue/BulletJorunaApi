from app import app,db
from app.models import User
from flask import request,abort,jsonify,url_for

@app.route('/users')
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username= username).first() is not None:
        abort(400)
    user = User(username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}

