from app.position import bp
from app.position.service import PositionService
from flask import request, jsonify


@bp.route('/')
def get_all():
    position_service = PositionService()
    positions = position_service.get()

    serialized_positions = [position.to_dict() for position in positions]

    return jsonify(serialized_positions), 200