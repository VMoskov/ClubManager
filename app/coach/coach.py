from app.extensions import db


class Coach(db.Model):
    id = db.Column('coach_id', db.Integer, primary_key=True)
    name = db.Column('first_name', db.String(64))
    surname = db.Column('last_name', db.String(64), index=True)
    birth_date = db.Column(db.Date)
    years_of_experience = db.Column(db.Integer)

    def __repr__(self):
        return f'<Coach {self.name} {self.surname}>'
    
    def to_dict(self):
        return {'id': self.id, 
                'name': f'{self.name} {self.surname}', 
                'birth_date': self.birth_date, 
                'years_of_experience': self.years_of_experience
                }