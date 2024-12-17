from app.player import bp
from app.player.service import PlayerService
from flask import request, jsonify
from app.utils import roles_required


@bp.route('/')
@roles_required(['admin', 'user'])
def get_all():
    '''
    Get all players
    ---
    tags:
        - player
    operationId: get_all_players
    responses:
        200:
            description: A list of all players
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                        name:
                            type: string
                        surname:
                            type: string
                        birth_date:
                            type: string
                        dominant_foot:
                            type: string
            examples:
                application/json: [{id: 1, name: 'John', surname: 'Doe', birth_date: '1990-01-01', dominant_foot: 'R'}, 
                                   {id: 2, name: 'Jane', surname: 'Doe', birth_date: '1995-01-01', dominant_foot: 'L'}]
        403:
            description: insufficient permissions
    '''
    player_service = PlayerService()
    players = player_service.get()

    serialized_players = [player.to_dict() for player in players]

    return jsonify(serialized_players), 200


@bp.route('/<int:id>')
@roles_required(['admin', 'user'])
def get_by_id(id):
    '''
    Get player by id
    ---
    tags:
        - player
    operationId: get_player_by_id
    parameters:
        - in: path
          name: player id
          required: true
          schema:
            type: integer
          description: Player id
    responses:
        200:
            description: A player
            schema:
                type: object
                properties:
                    id:
                        type: integer
                    name:
                        type: string
                    surname:
                        type: string
                    birth_date:
                        type: string
                    dominant_foot:
                        type: string
            examples:
                application/json: {id: 1, name: 'John', surname: 'Doe', birth_date: '1990-01-01', dominant_foot: 'R'}
        403: 
            descritpion: insufficient permissions   
        404:
            description: Player not found
    '''
    player_service = PlayerService()
    player = player_service.get(id)

    if player is None:
        return 'Player not found', 404
    
    serialized_player = player.to_dict()

    return jsonify(serialized_player), 200


@bp.route('/add', methods=['POST'])
@roles_required(['admin'])
def add():
    '''
    Add a player
    ---
    tags:
        - player
    operationId: add_player
    parameters:
        - in: body
          name: player
          required: true
          schema:
              type: object
              properties:
                  name:
                      type: string
                  surname:
                      type: string
                  birth_date:
                      type: string
                  dominant_foot:
                      type: string
    responses:
        201:
            description: Player added
        400:
            description: Bad request
        403:
            description: insufficient permissions
    '''
    player = request.get_json()
    player_service = PlayerService()
    
    try:
        player_service.add(player)
        return 'Player added', 201
    except ValueError as e:
        return str(e), 400


@bp.route('/update/<int:id>', methods=['PUT'])
@roles_required(['admin'])
def update(id):
    '''
    Update a player
    ---
    tags:
        - player
    operationId: update_player
    parameters:
        - in: path
          name: player id
          required: true
          schema:
              type: integer
          description: Player id
        - in: body
          name: player
          required: true
          schema:
              type: object
              properties:
                  name:
                      type: string
                  surname:
                      type: string
                  birth_date:
                      type: string
                  dominant_foot:
                      type: string
    responses:
        200:
            description: Player updated
        400:
            description: Invalid player
        403:
            description: insufficient permissions
    '''
    player = request.get_json()
    player_service = PlayerService()
    
    try:
        player_service.update(id, player)
        return 'Player updated', 200
    except ValueError as e:
        return str(e), 400


@bp.route('/delete/<int:id>', methods=['DELETE'])
@roles_required(['admin'])
def delete(id):
    '''
    Delete a player
    ---
    tags:
        - player
    operationId: delete_player
    parameters:
        - in: path
          name: player id
          required: true
          schema:
              type: integer
          description: Player id
    responses:
        200:
            description: Player deleted
        400:
            description: Invalid player
        403:
            description: insufficient permissions
    '''
    player_service = PlayerService()
    
    try:
        player_service.delete(id)
        return 'Player deleted', 200
    except ValueError as e:
        return str(e), 400