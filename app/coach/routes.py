from app.coach import bp
from app.coach.service import CoachService
from flask import request, jsonify
from app.utils import roles_required


@bp.route('/')
@roles_required(['admin', 'user'])
def get_all():
    '''
    Get all coaches
    ---
    tags:
        - coach
    operationId: get_all_coaches
    responses:
        200:
            description: A list of all coaches
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                        name:
                            type: string
                        birth_date:
                            type: string
                        years_of_experience:
                            type: integer
            examples:
                application/json: [{id: 1, name: 'John Doe', birth_date: '1990-01-01', years_of_experience: 5}, 
                                   {id: 2, name: 'Jane Doe', birth_date: '1995-01-01', years_of_experience: 3}]
        403:
            description: insufficient permissions
    '''
    coach_service = CoachService()
    coaches = coach_service.get()

    serialized_coaches = [coach.to_dict() for coach in coaches]

    return jsonify(serialized_coaches), 200


@bp.route('/<int:id>')
@roles_required(['admin', 'user'])
def get_by_id(id):
    '''
    Get coach by id
    ---
    tags:
        - coach
    operationId: get_coach_by_id
    parameters:
        - in: path
          name: coach id
          required: true
          schema:
              type: integer
          description: Coach id
    responses:
        200:
            description: A coach
            examples:
                application/json: {id: 1, name: 'John Doe', birth_date: '1990-01-01', years_of_experience: 5}
        403:
            description: insufficient permissions
        404:
            description: Coach not found
    '''
    coach_service = CoachService()
    coach = coach_service.get(id)

    if coach is None:
        return 'Coach not found', 404

    serialized_coach = coach.to_dict()

    return jsonify(serialized_coach), 200


@bp.route('/add', methods=['POST'])
@roles_required(['admin'])
def add():
    '''
    Add a coach
    ---
    tags:
        - coach
    operationId: add_coach
    parameters:
        - in: body
          name: coach
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
                  years_of_experience:
                      type: integer
          description: Coach data
    responses:
        201:
            description: Coach added
        400:
            description: Invalid coach or coach already exists
        403:
            description: insufficient permissions
    '''
    coach = request.get_json()
    coach_service = CoachService()

    try:
        coach_service.add(coach)
        return 'Coach added', 201
    except ValueError as e:
        return str(e), 400
    

@bp.route('/<int:id>/teams', methods=['GET'])
@roles_required(['admin', 'user'])
def get_teams(id):
    '''
    Get teams coached by a coach
    ---
    tags:
        - coach
    operationId: get_teams_by_coach
    parameters:
        - in: path
          name: coach id
          required: true
          schema:
              type: integer
          description: Coach id
    responses:
        200:
            description: A list of teams
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                        name:
                            type: string
            examples:
                application/json: [{id: 1, name: 'Team 1'}, {id: 2, name: 'Team 2'}]
        403:
            description: insufficient permissions
        404:
            description: Coach not found
    '''
    coach_service = CoachService()
    teams = coach_service.get_teams(id)

    if teams is None:
        return 'Coach not found', 404

    return jsonify(teams), 200


@bp.route('/update/<int:id>', methods=['PUT'])
@roles_required(['admin'])
def update(id):
    '''
    Update a coach
    ---
    tags:
        - coach
    operationId: update_coach
    parameters:
        - in: path
          name: coach id
          required: true
          schema:
              type: integer
          description: Coach id
        - in: body
          name: coach
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
                  years_of_experience:
                      type: integer
          description: Coach data
    responses:
        200:
            description: Coach updated
        400:
            description: Invalid coach
        403:
            description: insufficient permissions
    '''
    coach = request.get_json()
    coach_service = CoachService()

    try:
        coach_service.update(id, coach)
        return 'Coach updated', 200
    except ValueError as e:
        return str(e), 400
    

@bp.route('/delete/<int:id>', methods=['DELETE'])
@roles_required(['admin'])
def delete(id):
    '''
    Delete a coach
    ---
    tags:
        - coach
    operationId: delete_coach
    parameters:
        - in: path
          name: coach id
          required: true
          schema:
              type: integer
          description: Coach id
    responses:
        200:
            description: Coach deleted
        400:
            description: Coach not found
        403:
            description: insufficient permissions
    '''
    coach_service = CoachService()
    
    try:
        coach_service.delete(id)
        return 'Coach deleted', 200
    except ValueError as e:
        return str(e), 400