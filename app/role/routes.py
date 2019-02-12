from flask import jsonify
from flask_restful import Resource
from flask_jwt import jwt_required, current_identity


class Roles(Resource):

    @jwt_required()
    def get(self):
        return jsonify({'message': 'get Roles'})

    @jwt_required()
    def post(self):
        return jsonify({'message': 'post Roles'})


class Role(Resource):

    @jwt_required()
    def get(self,role_id):
        return jsonify({'message': 'get Role%s'%role_id})

    @jwt_required()
    def delete(self,role_id):
        return  jsonify({'message': 'delete Role%s'%role_id})