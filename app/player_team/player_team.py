from app.extensions import db


class PlayerTeam(db.Model):
    id = db.Column('player_team_id', db.Integer, primary_key=True)
    player_position = db.Column(db.String(64))
    kit_number = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    player = db.relationship('Player', backref='player_teams', lazy='true')
    team = db.relationship('Team', backref='player_teams', lazy='true')

    def __repr__(self):
        return f'<PlayerTeam {self.player_id} {self.team_id}>'