from app.coach import bp


@bp.route('/')
def index():
    return 'Welcome to the Coach Manager!'