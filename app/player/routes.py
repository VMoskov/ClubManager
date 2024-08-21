from app.player import bp


@bp.route('/')
def index():
    return 'Posts Index'


@bp.route('/categories/')
def categories():
    return 'Posts Categories'
