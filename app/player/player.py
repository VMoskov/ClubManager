from app.extensions import db


class Player(db.Model):
    id = db.Column('player_id', db.Integer, primary_key=True)
    name = db.Column('first_name', db.String(64))
    surname = db.Column('last_name', db.String(64), index=True)
    birth_date = db.Column(db.Date)
    dominant_foot = db.Column(db.String(1))

    def __repr__(self):
        return f'<Player {self.name} {self.surname}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'birth_date': self.birth_date,
            'dominant_foot': self.dominant_foot
        }