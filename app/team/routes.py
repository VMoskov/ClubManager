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


@bp.route('/<int:id>/coach', methods=['GET'])
def get_coach(id):
    team_service = TeamService()
    coach = team_service.get_coach(id)

    if coach is None:
        return 'Team not found', 404

    return jsonify(coach), 200