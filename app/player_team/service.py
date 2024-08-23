from app.extensions import db
from app.player.service import PlayerService
from app.team.service import TeamService
from app.position.service import PositionService
from app.player_team.player_team import PlayerTeam


class PlayerTeamService:
    def assign_player_to_team(self, player_id, team_id, body):
        player_service = PlayerService()
        team_service = TeamService()
        position_service = PositionService()

        if not self.is_valid(body):
            raise ValueError('Invalid player-team data')

        player = player_service.get(player_id)
        if player is None:
            raise ValueError('Player not found')
        
        team = team_service.get(team_id)
        if team is None:
            raise ValueError('Team not found')
        
        position = position_service.get(body['position_id'])
        if position is None:
            raise ValueError('Position not found')
        
        player_team = PlayerTeam(kit_number=body['kit_number'], player=player, team=team, position=position)
        db.session.add(player_team)
        db.session.commit()
        return player_team

    def is_valid(self, body):
        if body is None or not all(key in body for key in ['position_id', 'kit_number']):
            return False
        return True
