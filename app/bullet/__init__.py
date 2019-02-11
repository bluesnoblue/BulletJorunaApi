from flask import Blueprint

bp = Blueprint('bullet_journal', __name__)

from app.bullet import routes
