from flask import jsonify
from flask_restful import Resource
from flask_jwt import jwt_required, current_identity


class ResourcesTest(Resource):

    def get(self):
        return jsonify({'message': 'get ResourcesTest'})

    def post(self):
        return jsonify({'message': 'post ResourcesTest'})


class ResourceTest(Resource):

    @jwt_required()
    def get(self,resource_id):
        return jsonify({'message': 'get ResourceTest%s'%resource_id,
                        'user':current_identity.username})

    @jwt_required()
    def post(self,resource_id):
        return jsonify({'message': 'post ResourceTest%s'%resource_id,
                        'user': current_identity.username})

