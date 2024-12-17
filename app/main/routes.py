from app.main import bp


@bp.route('/')
def index():
    '''
    Home page
    ---
    tags:
        - main
    operationId: home
    responses:
        200:
            description: Welcome message
            schema:
                type: string
            examples:
                application/json: 'Welcome to the Club Manager'
    '''
    return 'Welcome to the Club Manager!'
