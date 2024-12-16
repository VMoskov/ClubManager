from app.player_team import bp
from app.player_team.service import PlayerTeamService
from flask import request
from app.utils import roles_required


@bp.route('/assign/<int:player_id>/<int:team_id>', methods=['POST'])
@roles_required(['admin'])
def assign_player_to_team(player_id, team_id):
    body = request.get_json()
    player_team_service = PlayerTeamService()

    try:
        player_team = player_team_service.assign_player_to_team(player_id, team_id, body)
        return 'Player assigned to the team', 201
    except ValueError as e:
        return str(e), 400
    