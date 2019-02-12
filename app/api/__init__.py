from .view import *
from flask_restful import Api
from flask import Blueprint

api = Blueprint("api", __name__)  # 设置蓝图
resource = Api(api)
#权限
resource.add_resource(Permissions, '/permissions')
#测试资源
resource.add_resource(ResourcesTest, '/resources')
resource.add_resource(ResourceTest, '/resource/<resource_id>')
#角色
resource.add_resource(Roles, '/roles')
resource.add_resource(Role, '/role/<role_id>')
