from app.extensions import db


class PlayerTeam(db.Model):
    __tablename__ = 'playerteam'

    id = db.Column('player_team_id', db.Integer, primary_key=True)
    kit_number = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))
    position_id = db.Column(db.Integer, db.ForeignKey('position.position_id'))
    player = db.relationship('Player', backref='player_teams', lazy=True)
    team = db.relationship('Team', backref='player_teams', lazy=True)
    position = db.relationship('Position', backref='player_teams', lazy=True)

    def __repr__(self):
        return f'<PlayerTeam {self.player_id} {self.team_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'kit_number': self.kit_number,
            'player_id': self.player_id,
            'team_id': self.team_id,
            'position_id': self.position_id
        }