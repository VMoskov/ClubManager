from flask import Blueprint

bp = Blueprint('position', __name__)

from app.position import routes