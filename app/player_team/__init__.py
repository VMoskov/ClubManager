from flask import Blueprint

bp = Blueprint('player_team', __name__)

from app.player_team import routes
