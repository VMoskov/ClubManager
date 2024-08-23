from app.player import bp
from app.player.service import PlayerService
from flask import request, jsonify


@bp.route('/')
def get_all():
    player_service = PlayerService()
    players = player_service.get()

    serialized_players = [player.to_dict() for player in players]

    return jsonify(serialized_players), 200


@bp.route('/<int:id>')
def get_by_id(id):
    player_service = PlayerService()
    player = player_service.get(id)

    if player is None:
        return 'Player not found', 404
    
    serialized_player = player.to_dict()

    return jsonify(serialized_player), 200


@bp.route('/add', methods=['POST'])
def add():
    player = request.get_json()
    player_service = PlayerService()
    
    try:
        player_service.add(player)
        return 'Player added', 201
    except ValueError as e:
        return str(e), 400


@bp.route('/<int:id>/update', methods=['PUT'])
def update(id):
    player = request.get_json()
    player_service = PlayerService()
    
    try:
        player_service.update(id, player)
        return 'Player updated', 200
    except ValueError as e:
        return str(e), 400


@bp.route('/<int:id>/delete', methods=['DELETE'])
def delete(id):
    player_service = PlayerService()
    
    try:
        player_service.delete(id)
        return 'Player deleted', 200
    except ValueError as e:
        return str(e), 400