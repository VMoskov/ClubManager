from flask import Flask

from config import Config
from app.extensions import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.player import bp as player_bp
    app.register_blueprint(player_bp, url_prefix='/player')

    from app.coach import bp as coach_bp
    app.register_blueprint(coach_bp, url_prefix='/coach')

    from app.team import bp as team_bp
    app.register_blueprint(team_bp, url_prefix='/team')

    from app.player_team import bp as player_team_bp
    app.register_blueprint(player_team_bp, url_prefix='/player_team')

    from app.position import bp as position_bp
    app.register_blueprint(position_bp, url_prefix='/position')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
