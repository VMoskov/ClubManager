from app.team import bp


@bp.route('/')
def index():
    return 'Welcome to the Team Manager!'