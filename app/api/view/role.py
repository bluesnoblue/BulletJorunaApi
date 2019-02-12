from flask import request,jsonify,abort
from flask_restful import Resource
from flask_jwt import jwt_required
from app import db,models

class Roles(Resource):

    @jwt_required()
    def get(self):
        roles = []
        for role in models.Role.query.all():
            roles.append({'id': role.id, 'name': role.name})
        return jsonify(roles)

    @jwt_required()
    def post(self):
        name = request.form.get('name')
        permission_ids = request.form.get('permissions').split(',')
        if not name or models.Role.query.filter_by(name=name).first():
            abort(400)
        r = models.Role(name=name)
        db.session.add(r)

        for permission_id in permission_ids:
            if not models.Permission.query.filter_by(id=permission_id).first():
                abort(400)
            rp = models.RolePermissons()
            rp.permission_id = permission_id
            rp.role_id = r.id
            db.session.add(rp)

        db.session.commit()
        return jsonify({'id':r.id,'name':r.name})


class Role(Resource):

    @jwt_required()
    def get(self,role_id):
        r = models.Role.query.filter_by(id=role_id).first()
        return jsonify({'id': r.id, 'name': r.name})

    @jwt_required()
    def delete(self,role_id):
        role = models.Role.query.filter_by(id=role_id).first()
        rps = models.RolePermissons.query.filter_by(role_id=role_id).all()
        if not role:
            abort(400)
        # print(role)
        db.session.delete(role)
        for rp in rps:
            db.session.delete(rp)
        db.session.commit()
        return 204