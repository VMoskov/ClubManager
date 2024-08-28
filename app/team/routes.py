from app.team import bp
from app.team.service import TeamService
from flask import request, jsonify


@bp.route('/', methods=['GET'])
def get_all():
    team_service = TeamService()
    teams = team_service.get()

    serialized_teams = [team.to_dict() for team in teams]

    return jsonify(serialized_teams), 200


@bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    team_service = TeamService()
    team = team_service.get(id)

    if team is None:
        return 'Team not found', 404

    serialized_team = team.to_dict()

    return jsonify(serialized_team), 200


@bp.route('/add', methods=['POST'])
def add():
    team = request.get_json()
    team_service = TeamService()
    
    try:
        team_service.add(team)
        return 'Team added', 201
    except ValueError as e:
        return str(e), 400


@bp.route('/<int:id>/players', methods=['GET'])
def get_players(id):
    team_service = TeamService()
    players = team_service.get_players(id)

    if players is None:
        return 'Team not found', 404

    return jsonify(players), 200


@bp.route('/<int:team_id>/players/<int:position_id>', methods=['GET'])
def get_players_by_position(team_id, position_id):
    team_service = TeamService()
    players = team_service.get_players_by_position(team_id, position_id)

    if players is None:
        return 'Team not found', 404

    return jsonify(players), 200


@bp.route('/<int:team_id>/home_stadium', methods=['GET'])
def get_home_stadium(team_id):
    team_service = TeamService()
    home_stadium = team_service.get_home_stadium(team_id)

    if home_stadium is None:
        return 'Team not found', 404

    return jsonify(home_stadium), 200


@bp.route('/<int:team_id>/assign_coach/<int:coach_id>', methods=['PUT'])
def assign_coach(team_id, coach_id):
    team_service = TeamService()
    team = team_service.assign_coach(team_id, coach_id)

    if team is None:
        return 'Team not found', 404

    return 'Coach assigned', 200


@bp.route('/<int:id>/coach', methods=['GET'])
def get_coach(id):
    team_service = TeamService()
    coach = team_service.get_coach(id)

    if coach is None:
        return 'Team not found', 404

    return jsonify(coach), 200


@bp.route('/<int:id>/delete_coach', methods=['DELETE'])
def delete_coach(id):
    team_service = TeamService()
    team = team_service.delete_coach(id)

    if team is None:
        return 'Team not found', 404

    return 'Coach deleted', 200


@bp.route('/<int:id>/update', methods=['PUT'])
def update(id):
    team = request.get_json()
    team_service = TeamService()
    
    try:
        team_service.update(id, team)
        return 'Team updated', 200
    except ValueError as e:
        return str(e), 400


@bp.route('/<int:id>/delete', methods=['DELETE'])
def delete(id):
    team_service = TeamService()
    team = team_service.delete(id)

    if team is None:
        return 'Team not found', 404

    return 'Team deleted', 200