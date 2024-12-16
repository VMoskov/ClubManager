from app.extensions import db


class User(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(64), unique=True)
    email = db.Column('email', db.String(64), unique=True)
    password = db.Column('pass', db.String(128))
    name = db.Column('first_name', db.String(64))
    surname = db.Column('last_name', db.String(64))
    birth_date = db.Column('birth_date', db.Date)
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'))
    role = db.relationship('Role', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role.to_dict()
        }