from app.player_team import bp


@bp.route('/')
def index():
    return 'Welcome to the Player Team Manager!'