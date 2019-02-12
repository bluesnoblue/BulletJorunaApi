from flask import Blueprint

bp = Blueprint('role', __name__)

from app.role import routes
