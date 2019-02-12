from flask import request,jsonify,abort
from flask_restful import Resource
from flask_jwt import jwt_required
from app.models import Permission
from app import db

class Permissions(Resource):

    @jwt_required()
    def get(self):
        permissions =[]
        for permission in Permission.query.all():
            permissions.append({'id':permission.id,'name':permission.name})
        return jsonify(permissions)

    @jwt_required()
    def post(self):
        name = request.form.get('name')
        parent_id = request.form.get('parent_id')
        if not name or Permission.query.filter_by(name=name).first():
            abort(400)
        if not parent_id :
            root = Permission.query.filter_by(name='root').first()
            parent_id = root.id if root else None
        p = Permission(name,parent_id)
        db.session.add(p)
        db.session.commit()
        return jsonify({'id':p.id,'name':p.name})