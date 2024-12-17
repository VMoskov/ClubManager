from app.position import bp
from app.position.service import PositionService
from flask import request, jsonify
from app.utils import roles_required


@bp.route('/')
@roles_required(['admin', 'user'])
def get_all():
    '''
    Get all positions
    ---
    tags:
        - position
    operationId: get_all_positions
    responses:
        200:
            description: A list of all positions
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                        name:
                            type: string
                        description:
                            type: string
                        salary:
                            type: integer
            examples:
                application/json: [{id: 1, name: 'Software Engineer', description: 'Develop software', salary: 100000}, 
                                   {id: 2, name: 'Data Scientist', description: 'Analyze data', salary: 120000}]
        403:
            description: insufficient permissions
    '''
    position_service = PositionService()
    positions = position_service.get()

    serialized_positions = [position.to_dict() for position in positions]

    return jsonify(serialized_positions), 200