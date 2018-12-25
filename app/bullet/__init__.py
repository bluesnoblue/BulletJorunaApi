from flask import Blueprint

bp = Blueprint('bullet', __name__)

from app.bullet import routes
