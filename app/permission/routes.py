from flask import jsonify
from flask_restful import Resource
from flask_jwt import jwt_required, current_identity
# from app.public.permission import *


class Permissions(Resource):

    @jwt_required()
    def get(self):
        return jsonify({'message': 'get permissions'})
