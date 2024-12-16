from app.coach import bp
from app.coach.service import CoachService
from flask import request, jsonify
from app.utils import roles_required


@bp.route('/')
@roles_required(['admin', 'user'])
def get_all():
    coach_service = CoachService()
    coaches = coach_service.get()

    serialized_coaches = [coach.to_dict() for coach in coaches]

    return jsonify(serialized_coaches), 200


@bp.route('/<int:id>')
@roles_required(['admin', 'user'])
def get_by_id(id):
    coach_service = CoachService()
    coach = coach_service.get(id)

    if coach is None:
        return 'Coach not found', 404

    serialized_coach = coach.to_dict()

    return jsonify(serialized_coach), 200


@bp.route('/add', methods=['POST'])
@roles_required(['admin'])
def add():
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
    coach_service = CoachService()
    teams = coach_service.get_teams(id)

    if teams is None:
        return 'Coach not found', 404

    return jsonify(teams), 200


@bp.route('/update/<int:id>', methods=['PUT'])
@roles_required(['admin'])
def update(id):
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
    coach_service = CoachService()
    
    try:
        coach_service.delete(id)
        return 'Coach deleted', 200
    except ValueError as e:
        return str(e), 400