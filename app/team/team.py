from app.extensions import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    home_stadium = db.Column(db.String(64))
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'))
    trainer = db.relationship('Trainer', backref='teams', lazy='true')

    def __repr__(self):
        return f'<Team {self.name} from {self.city}, {self.country}>'