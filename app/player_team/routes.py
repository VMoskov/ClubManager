from app.player_team import bp
from app.player_team.service import PlayerTeamService
from flask import request
from app.utils import roles_required


@bp.route('/assign/<int:player_id>/<int:team_id>', methods=['POST'])
@roles_required(['admin'])
def assign_player_to_team(player_id, team_id):
    '''
    Assign player to team
    ---
    tags:
        - player_team
    operationId: assign_player_to_team
    parameters:
        - in: path
          name: player_id
          required: true
          schema:
              type: integer
        - in: path
          name: team_id
          required: true
          schema:
              type: integer
        - in: body
          name: player_team
          required: true
          schema:
              type: object
              properties:
                  number:
                      type: integer
                  position:
                      type: string
          description: Player team data
    '''
    body = request.get_json()
    player_team_service = PlayerTeamService()

    try:
        player_team = player_team_service.assign_player_to_team(player_id, team_id, body)
        return 'Player assigned to the team', 201
    except ValueError as e:
        return str(e), 400
    