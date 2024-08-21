from app.extensions import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64), index=True)
    birthday = db.Column(db.Date)
    dominant_foot = db.Column(db.String(1))

    def __repr__(self):
        return f'<Player {self.name} {self.surname}>'