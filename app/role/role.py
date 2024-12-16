from app.extensions import db


class Role(db.Model):
    __tablename__ = 'AppRole'

    id = db.Column('role_id', db.Integer, primary_key=True)
    name = db.Column('role_name', db.String(64), unique=True)

    def __repr__(self):
        return f'<Role {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }