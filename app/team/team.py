from app.extensions import db
from app.coach.coach import Coach


class Team(db.Model):
    id = db.Column('team_id', db.Integer, primary_key=True)
    name = db.Column('team_name', db.String(64), unique=True)
    home_stadium = db.Column(db.String(64))
    coach_id = db.Column(db.Integer, db.ForeignKey('coach.coach_id'))
    coach = db.relationship('Coach', backref='teams', lazy=True)

    def __repr__(self):
        return f'<Team {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'team_name': self.name,
            'home_stadium': self.home_stadium,
            'coach': f'{self.coach.name} {self.coach.surname}' if self.coach is not None else None
        }