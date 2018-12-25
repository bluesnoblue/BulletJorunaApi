from app import db
from app.bullet import bp
from app.models import Bullet
from flask import request, jsonify
from flask_jwt import jwt_required, current_identity


@bp.route('/bullets', methods=['GET'])
@jwt_required()
def get_bullets():
    print('get_bullets')
    bullets = []
    for bullet in Bullet.query.filter_by(user_id=current_identity.id):
        print(bullet)
        bullets.append({'id': bullet.id, 'mark': bullet.mark, 'type': bullet.bullet_type,
                        'body': bullet.body, 'time': bullet.timestamp})
    return jsonify({'data': bullets}), 201


@bp.route('/bullets', methods=['POST'])
@jwt_required()
def post_bullet():
    body = request.form.get('body')
    bullet_type = request.form.get('type')
    user_id = current_identity.id
    bullet = Bullet(bullet_type, body, user_id)
    db.session.add(bullet)
    db.session.commit()
    return jsonify({
        'id': bullet.id,
        'mark': bullet.mark,
        'type': bullet.bullet_type,
        'body': bullet.body,
        'time': bullet.timestamp,
    }), 201




