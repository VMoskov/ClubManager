from app.extensions import db


class Team(db.Model):
    id = db.Column('team_id', db.Integer, primary_key=True)
    name = db.Column('team_name', db.String(64))
    home_stadium = db.Column(db.String(64))
    coach_id = db.Column(db.Integer, db.ForeignKey('coach.id'))
    coach = db.relationship('Coach', backref='teams', lazy='true')

    def __repr__(self):
        return f'<Team {self.name} from {self.city}, {self.country}>'