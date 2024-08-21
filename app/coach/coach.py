from app.extensions import db


class Coach(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64), index=True)
    birthday = db.Column(db.Date)
    years_of_experience = db.Column(db.Integer)

    def __repr__(self):
        return f'<Coach {self.name} {self.surname}>'