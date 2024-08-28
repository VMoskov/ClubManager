from app.extensions import db
from app.team.team import Team
from app.coach.coach import Coach


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
    
    def get_players(self, id):
        from app.player_team.player_team import PlayerTeam

        team = Team.query.get(id)
        if team is None:
            return None
        
        entries = PlayerTeam.query.filter_by(team_id=team.id).all()
        team_players = [entry.player for entry in entries]
        positions = [entry.position for entry in entries]
        kit_numbers = [entry.kit_number for entry in entries]     

        number_of_players = len(team_players)   

        return {'id': id, 'name': team.name, 'number of players': number_of_players, 'players': 
                [{'player': f'{player.name} {player.surname}', 'position': position.name, 'kit_number': kit_number} 
                 for player, position, kit_number in zip(team_players, positions, kit_numbers)]}
    
    def assign_coach(self, team_id, coach_id):
        team = Team.query.get(team_id)
        if team is None:
            return None
        
        coach = Coach.query.get(coach_id)
        if coach is None:
            return None
        
        team.coach = coach
        db.session.commit()
        return team
    
    def get_coach(self, id):
        team = Team.query.get(id)
        if team is None:
            return None
        
        coach = team.coach
        return {'id': coach.id, 'name': f'{coach.name} {coach.surname}'}
    
    def delete_coach(self, id):
        team = Team.query.get(id)
        if team is None:
            return None
        
        team.coach = None
        db.session.commit()
        return team
    
    def update(self, id, team):
        if not self.is_valid(team):
            raise ValueError('Invalid team')
        
        team_to_update = Team.query.get(id)
        if team_to_update is None:
            return None
        
        team_to_update.name = team['name']
        team_to_update.home_stadium = team['home_stadium']
        team_to_update.coach_id = team['coach_id']
        if team_to_update.coach_id == 'null':
            team_to_update.coach_id = None

        if self.already_exists(team_to_update):
            raise ValueError('Team already exists')
        
        db.session.commit()
        return team_to_update
    
    def delete(self, id):
        team = Team.query.get(id)
        if team is None:
            return None
        
        db.session.delete(team)
        db.session.commit()
        return team
    
    def is_valid(self, team):
        if team is None or not all(key in team for key in ['name', 'home_stadium', 'coach_id']):
            return False
        return True
        
    def already_exists(self, team):
        return db.session.query(Team).filter_by(name=team.name).first() is not None