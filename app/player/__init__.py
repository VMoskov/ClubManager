from flask import Blueprint
from app.player import routes

bp = Blueprint('player', __name__)