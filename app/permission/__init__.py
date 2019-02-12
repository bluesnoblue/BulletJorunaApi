from flask import Blueprint

bp = Blueprint('permission', __name__)

from app.permission import routes
