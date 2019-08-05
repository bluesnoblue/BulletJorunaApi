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
    content = request.form.get('content')
    bullet_type = request.form.get('type')
    user_id = current_identity.id
    timestamp = 0
    bullet = Bullet(bullet_type, content, user_id, timestamp)
    db.session.add(bullet)
    db.session.commit()
    return jsonify({
        'id': bullet.id,
        'mark': bullet.mark,
        'type': bullet.bullet_type,
        'body': bullet.body,
        'time': bullet.timestamp,
    }), 201


@bp.route('/bullet/<bullet_id>', methods=['PATCH'])
@jwt_required()
def update_bullet():
    return 204


@bp.route('/bullet/<bullet_id>', methods=['DELETE'])
@jwt_required()
def update_bullet():
    return 204


@bp.route('/bullet/<bullet_id>/reopen', methods=['POST'])
@jwt_required()
def update_bullet():
    return 204


@bp.route('/bullet/<bullet_id>/delay', methods=['POST'])
@jwt_required()
def delay_bullet():
    return 204


@bp.route('/bullet/<bullet_id>/cancel', methods=['POST'])
@jwt_required()
def cancel_bullet():
    return 204



