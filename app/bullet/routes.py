from app import db
from app.bullet import bp
from app.models import Bullet
from flask import request, jsonify
from flask_jwt import jwt_required, current_identity


@bp.route('/bullets', methods=['GET'])
@jwt_required()
def get_bullets():
    bullets = []
    for bullet in Bullet.query.filter_by(user_id=current_identity.id):

        bullets.append(
            {
                'id': bullet.id,
                'type': bullet.bullet_type,
                'status':bullet.status,
                'content': bullet.content,
                'time': bullet.timestamp})

    return jsonify({'data': bullets}), 200


@bp.route('/bullets', methods=['POST'])
@jwt_required()
def post_bullet():
    values = request.get_json()
    required = ['type', 'content']
    if not values:
        return jsonify({'error': 'Miss Values'}), 499
    if not all(k in values for k in required):
        return jsonify({'error': 'Miss Values'}), 499

    bullet_type = values['type']
    content = values['content']
    user_id = current_identity.id
    timestamp = values.get('timestamp') or 0

    bullet = Bullet(bullet_type, content, user_id, timestamp)
    db.session.add(bullet)
    db.session.commit()

    return jsonify(
        {
            'id': bullet.id,
            'type': bullet.bullet_type,
            'content': bullet.content,
            'time': bullet.timestamp
        }
    ), 201


@bp.route('/bullet/<bullet_id>', methods=['PATCH'])
@jwt_required()
def update_bullet(bullet_id):
    values = request.get_json()
    if not values:
        return jsonify({'error': 'Miss Values'}), 499
    content = values.get('content')
    timestamp = values.get('timestamp') or 0
    bullet = Bullet.query.filter_by(user_id=current_identity.id, id=bullet_id).first()
    if not bullet:
        return jsonify({'error': 'bullet is not exist'}), 499
    if content:
        bullet.update_body(content)
    if timestamp:
        bullet.set_timestamp(timestamp)
    db.session.commit()
    return jsonify(
        {
            'id': bullet.id,
            'type': bullet.bullet_type,
            'content': bullet.content,
            'time': bullet.timestamp
        }
    ), 200


@bp.route('/bullet/<bullet_id>', methods=['DELETE'])
@jwt_required()
def delete_bullet(bullet_id):
    bullet = Bullet.query.filter_by(user_id=current_identity.id, id=bullet_id).first()
    if not bullet:
        return jsonify({'error': 'bullet is not exist'}), 499
    db.session.delete(bullet)
    db.session.commit()
    return jsonify(), 204


@bp.route('/bullet/<bullet_id>/delay', methods=['POST'])
@jwt_required()
def delay_bullet(bullet_id):
    values = request.get_json()
    required = ['timestamp']
    if not values:
        return jsonify({'error': 'Miss Values'}), 499
    if not all(k in values for k in required):
        return jsonify({'error': 'Miss Values'}), 499

    bullet = Bullet.query.filter_by(id=bullet_id, user_id=current_identity.id).first()
    if not bullet:
        return jsonify({'error': 'bullet is not exist'}), 499
    if bullet.status != 0:
        return jsonify({'error': 'bullet can not delay'}), 499
    bullet.delay()
    db.session.commit()
    return jsonify(), 204


@bp.route('/bullet/<bullet_id>/cancel', methods=['POST'])
@jwt_required()
def cancel_bullet(bullet_id):
    bullet = Bullet.query.filter_by(id=bullet_id, user_id=current_identity.id).first()
    if not bullet:
        return jsonify({'error': 'bullet is not exist'}), 499
    if bullet.status != 0:
        return jsonify({'error': 'bullet can not cancel'}), 499
    bullet.cancel()
    db.session.commit()
    return jsonify(), 204


@bp.route('/bullet/<bullet_id>/finish', methods=['POST'])
@jwt_required()
def finish_bullet(bullet_id):
    bullet = Bullet.query.filter_by(id=bullet_id, user_id=current_identity.id).first()
    if not bullet:
        return jsonify({'error': 'bullet is not exist'}), 499
    if bullet.status != 0:
        return jsonify({'error': 'bullet can not finish'}), 499
    bullet.finish()
    db.session.commit()
    return jsonify(), 204


@bp.route('/bullet/<bullet_id>/reopen', methods=['POST'])
@jwt_required()
def reopen_bullet(bullet_id):
    bullet = Bullet.query.filter_by(id=bullet_id, user_id=current_identity.id).first()
    if not bullet:
        return jsonify({'error': 'bullet is not exist'}), 499
    if bullet.status not in [1, 2]:
        return jsonify({'error': 'bullet can not reopen'}), 499
    bullet.reopen()
    db.session.commit()
    return jsonify(), 204
