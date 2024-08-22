from app.position import bp


@bp.route('/')
def index():
    return 'Welcome to the Position Manager!'