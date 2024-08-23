from app.player_team import bp
from app.player_team.service import PlayerTeamService
from flask import request


@bp.route('/')
def index():
    return 'Welcome to the Player Team Manager!'


@bp.route('/assign/<int:player_id>/<int:team_id>', methods=['POST'])
def assign_player_to_team(player_id, team_id):
    body = request.get_json()
    player_team_service = PlayerTeamService()

    try:
        player_team = player_team_service.assign_player_to_team(player_id, team_id, body)
        return 'Player assigned to the team', 201
    except ValueError as e:
        return str(e), 400
    