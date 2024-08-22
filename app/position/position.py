from app.extensions import db


class Position(db.Model):
    id = db.Column('position_id', db.Integer, primary_key=True)
    name = db.Column('position_name', db.String(64), index=True, unique=True)

    def __repr__(self):
        return f'<Position {self.name}>'
    
    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
        }
        return data