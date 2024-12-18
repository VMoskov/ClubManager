from app.team import bp
from app.team.service import TeamService
from flask import request, jsonify
from app.utils import roles_required


@bp.route('/', methods=['GET'])
@roles_required(['admin', 'user'])
def get_all():
    '''
    Get all teams
    ---
    tags:
        - team
    operationId: get_all_teams
    responses:
        200:
            description: A list of all teams
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                        name:
                            type: string
                        home_stadium:
                            type: string
                        coach_id:
                            type: integer
            examples:
                application/json: [{id: 1, name: 'Team A', home_stadium: 'Stadium A', coach_id: 1}, 
                                   {id: 2, name: 'Team B', home_stadium: 'Stadium B', coach_id: 2}]
        403:
            description: insufficient permissions
    '''
    team_service = TeamService()
    teams = team_service.get()

    serialized_teams = [team.to_dict() for team in teams]

    return jsonify(serialized_teams), 200


@bp.route('/<int:id>', methods=['GET'])
@roles_required(['admin', 'user'])
def get_by_id(id):
    '''
    Get team by id
    ---
    tags:
        - team
    operationId: get_team_by_id
    parameters:
        - in: path
          name: team id
          required: true
    responses:
        200:
            description: A team
            schema:
                type: object
                properties:
                    id:
                        type: integer
                    name:
                        type: string
                    home_stadium:
                        type: string
                    coach_id:
                        type: integer
            examples:
                application/json: {id: 1, name: 'Team A', home_stadium: 'Stadium A', coach_id: 1}
        403:
            description: insufficient permissions
        404:
            description: Team not found
    '''
    team_service = TeamService()
    team = team_service.get(id)

    if team is None:
        return 'Team not found', 404

    serialized_team = team.to_dict()

    return jsonify(serialized_team), 200


@bp.route('/add', methods=['POST'])
@roles_required(['admin'])
def add():
    '''
    Add team
    ---
    tags:
        - team
    operationId: add_team
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        name:
                            type: string
                        home_stadium:
                            type: string
                        coach_id:
                            type: integer
                    required:
                        - name
                        - home_stadium
                        - coach_id
                examples:
                    application/json: {name: 'Team A', home_stadium: 'Stadium A', coach_id: 1}
    responses:
        201:
            description: Team added
        400:
            description: Invalid team
        400:
            description: Team already exists
        403:
            description: insufficient permissions
    '''
    team = request.get_json()
    team_service = TeamService()
    
    try:
        team_service.add(team)
        return 'Team added', 201
    except ValueError as e:
        return str(e), 400


@bp.route('/<int:id>/players', methods=['GET'])
@roles_required(['admin', 'user'])
def get_players(id):
    '''
    Get players of a team
    ---
    tags:
        - team
    operationId: get_players
    parameters:
        - in: path
          name: team id
          required: true
    responses:
        200:
            description: A list of players
            schema:
                type: array
                items:
                    type: object
                    properties:
                        player:
                            type: string
                        position:
                            type: string
                        kit_number:
                            type: integer
            examples:
                application/json: [{player: 'John Doe', position: 'Goalkeeper', kit_number: 1}, 
                                   {player: 'Jane Doe', position: 'Defender', kit_number: 2}]
        403:
            description: insufficient permissions
        404:
            description: Team not found
    '''
    team_service = TeamService()
    players = [player.to_dict() for player in team_service.get_players(id)]

    if players is None:
        return 'Team not found', 404

    return jsonify(players), 200


@bp.route('/<int:team_id>/players/<int:position_id>', methods=['GET'])
@roles_required(['admin', 'user'])
def get_players_by_position(team_id, position_id):
    '''
    Get players of a team by position
    ---
    tags:
        - team
    operationId: get_players_by_position
    parameters:
        - in: path
          name: team id
          required: true
        - in: path
          name: position id
          required: true
    responses:
        200:
            description: A list of players
            schema:
                type: array
                items:
                    type: object
                    properties:
                        player:
                            type: string
                        kit_number:
                            type: integer
            examples:
                application/json: [{player: 'John Doe', kit_number: 1}, 
                                   {player: 'Jane Doe', kit_number: 2}]
        403:
            description: insufficient permissions
        404:
            description: Team not found
    '''
    team_service = TeamService()
    players = [player.to_dict() for player in team_service.get_players_by_position(team_id, position_id)]

    if players is None:
        return 'Team not found', 404

    return jsonify(players), 200


@bp.route('/<int:team_id>/home_stadium', methods=['GET'])
@roles_required(['admin', 'user'])
def get_home_stadium(team_id):
    '''
    Get home stadium of a team
    ---
    tags:
        - team
    operationId: get_home_stadium
    parameters:
        - in: path
          name: team id
          required: true
    responses:
        200:
            description: Home stadium
            schema:
                type: object
                properties:
                    id:
                        type: integer
                    team:
                        type: string
                    home_stadium:
                        type: string
            examples:
                application/json: {id: 1, team: 'Team A', home_stadium: 'Stadium A'}
        403:
            description: insufficient permissions
        404:
            description: Team not found
    '''
    team_service = TeamService()
    home_stadium = team_service.get_home_stadium(team_id)

    if home_stadium is None:
        return 'Team not found', 404

    return jsonify(home_stadium.to_dict()), 200


@bp.route('/<int:team_id>/assign_coach/<int:coach_id>', methods=['PUT'])
@roles_required(['admin'])
def assign_coach(team_id, coach_id):
    '''
    Assign coach to a team
    ---
    tags:
        - team
    operationId: assign_coach
    parameters:
        - in: path
          name: team id
          required: true
        - in: path
          name: coach id
          required: true
    responses:
        200:
            description: Coach assigned
        404:
            description: Team not found
        404:
            description: Coach not found
        403:
            description: insufficient permissions
    '''
    team_service = TeamService()
    team = team_service.assign_coach(team_id, coach_id)

    if team is None:
        return 'Team not found', 404

    return 'Coach assigned', 200


@bp.route('/<int:id>/coach', methods=['GET'])
@roles_required(['admin', 'user'])
def get_coach(id):
    '''
    Get coach of a team
    ---
    tags:
        - team
    operationId: get_coach
    parameters:
        - in: path
          name: team id
          required: true
    responses:
        200:
            description: Coach
            schema:
                type: object
                properties:
                    id:
                        type: integer
                    name:
                        type: string
            examples:
                application/json: {id: 1, name: 'John Doe'}
        403:
            description: insufficient permissions
        404:
            description: Team not found
    '''
    team_service = TeamService()
    coach = team_service.get_coach(id)

    if coach is None:
        return 'Team not found', 404

    return jsonify(coach.to_dict()), 200


@bp.route('/<int:id>/delete_coach', methods=['DELETE'])
@roles_required(['admin'])
def delete_coach(id):
    '''
    Delete coach from a team
    ---
    tags:
        - team
    operationId: delete_coach
    parameters:
        - in: path
          name: team id
          required: true
    responses:
        200:
            description: Coach deleted
        404:
            description: Team not found
        403:
            description: insufficient permissions
    '''
    team_service = TeamService()
    team = team_service.delete_coach(id)

    if team is None:
        return 'Team not found', 404

    return 'Coach deleted', 200


@bp.route('/<int:id>/update', methods=['PUT'])
@roles_required(['admin'])
def update(id):
    '''
    Update team
    ---
    tags:
        - team
    operationId: update_team
    parameters:
        - in: path
          name: team id
          required: true
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        name:
                            type: string
                        home_stadium:
                            type: string
                        coach_id:
                            type: integer
                    required:
                        - name
                        - home_stadium
                        - coach_id
                examples:
                    application/json: {name: 'Team A', home_stadium: 'Stadium A', coach_id: 1}
    responses:
        200:
            description: Team updated
        400:
            description: Invalid team
        400:
            description: Team already exists
        404:
            description: Team not found
        403:
            description: insufficient permissions
    '''
    team = request.get_json()
    team_service = TeamService()
    
    try:
        team_service.update(id, team)
        return 'Team updated', 200
    except ValueError as e:
        return str(e), 400


@bp.route('/<int:id>/delete', methods=['DELETE'])
@roles_required(['admin'])
def delete(id):
    '''
    Delete team
    ---
    tags:
        - team
    operationId: delete_team
    parameters:
        - in: path
          name: team id
          required: true
    responses:
        200:
            description: Team deleted
        404:
            description: Team not found
        403:
            description: insufficient permissions
    '''
    team_service = TeamService()
    team = team_service.delete(id)

    if team is None:
        return 'Team not found', 404

    return 'Team deleted', 200