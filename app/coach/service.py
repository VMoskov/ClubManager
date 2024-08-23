from app.extensions import db
from app.coach.coach import Coach


class CoachService:
    def add(self, coach):
        if not self.is_valid(coach):
            raise ValueError('Invalid coach')
        
        coach = Coach(name=coach['name'], surname=coach['surname'], birth_date=coach['birth_date'], 
                      years_of_experience=coach['years_of_experience'])
        
        if coach.birth_date == 'null':
            coach.birth_date = None
        
        if coach.birth_date is not None and coach.birth_date > db.func.current_date():
            raise ValueError('Birth date cannot be in the future')
        
        if self.already_exists(coach):
            raise ValueError('Coach already exists')
        
        db.session.add(coach)
        db.session.commit()
        return coach
    
    def get(self, id=None):
        if id is None:
            return Coach.query.all()
        return Coach.query.get(id)
    
    def update(self, id, coach):
        if not self.is_valid(coach):
            raise ValueError('Invalid coach')
        
        coach_to_update = Coach.query.get(id)
        if coach_to_update is None:
            return None
        
        coach_to_update.name = coach['name']
        coach_to_update.surname = coach['surname']
        coach_to_update.birth_date = coach['birth_date']
        coach_to_update.years_of_experience = coach['years_of_experience']
        
        db.session.commit()
        return coach_to_update
    
    def is_valid(self, coach):
        if not isinstance(coach, dict):
            return False
        if 'name' not in coach or 'surname' not in coach or 'birth_date' not in coach or 'years_of_experience' not in coach:
            return False
        return True
    
    def already_exists(self, coach):
        return Coach.query.filter_by(name=coach.name, surname=coach.surname).first() is not None