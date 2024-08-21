from app.extensions import db


class Player(db.Model):
    id = db.Column('player_id', db.Integer, primary_key=True)
    name = db.Column('first_name', db.String(64))
    surname = db.Column('last_name', db.String(64), index=True)
    birth_date = db.Column(db.Date)
    dominant_foot = db.Column(db.String(1))

    def __repr__(self):
        return f'<Player {self.name} {self.surname}>'