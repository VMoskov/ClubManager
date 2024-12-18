from unittest.mock import MagicMock, patch
from app.player_team.service import PlayerTeamService


def test_assign_player_to_team():
    mocked_player = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', dominant_foot='R')
    mocked_team = MagicMock(id=1, name='Team 1')
    mocked_position = MagicMock(id=1, name='GK')
    mocked_player_team = MagicMock(id=1, 
                                   kit_number=1, 
                                   player=mocked_player,
                                   team=mocked_team,
                                   position=mocked_position,
                                   to_dict=lambda: {
                                      'id': 1,
                                      'kit_number': 1,
                                      'player': {'id': 1, 'name': 'John Doe', 'birth_date': '1990-01-01', 'dominant_foot': 'R'},
                                      'team': {'id': 1, 'name': 'Team 1'},
                                      'position': {'id': 1, 'name': 'Goalkeeper'}
                                      }
                                  )

    with patch('app.player_team.service.PlayerTeamService.assign_player_to_team', return_value=mocked_player_team):
        with patch('app.player.service.PlayerService.get', return_value=mocked_player):
            with patch('app.team.service.TeamService.get', return_value=mocked_team):
                with patch('app.position.service.PositionService.get', return_value=mocked_position):
                    player_teams = PlayerTeamService().assign_player_to_team(player_id=1, team_id=1, body={'position_id': 1, 'kit_number': 1})
                    assert player_teams == mocked_player_team