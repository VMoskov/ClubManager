from app.extensions import db
from app.team.team import Team

class TeamService:
    def add(self, team):
        if not self.is_valid(team):
            raise ValueError('Invalid team')
        
        team = Team(name=team['name'], home_stadium=team['home_stadium'], coach_id=team['coach_id'])
        if team.coach_id == 'null':
            team.coach_id = None

        if self.already_exists(team):
            raise ValueError('Team already exists')
        
        db.session.add(team)
        db.session.commit()
        return team
    
    def get(self, id=None):
        if id is None:
            return Team.query.all()
        return Team.query.get(id)
    
    def is_valid(self, team):
        if team is None or not all(key in team for key in ['name', 'home_stadium', 'coach_id']):
            return False
        return True
        
    def already_exists(self, team):
        return db.session.query(Team).filter_by(name=team.name).first() is not None
    
