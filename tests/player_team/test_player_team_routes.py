from unittest.mock import MagicMock, patch


def test_assign_player_to_team(app):
    success = 'Player assigned to the team'
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

    with patch('app.player_team.service.PlayerTeamService.assign_player_to_team', return_value=success):
        with patch('app.player.service.PlayerService.get', return_value=mocked_player):
            with patch('app.team.service.TeamService.get', return_value=mocked_team):
                with patch('app.position.service.PositionService.get', return_value=mocked_position):
                    response = app.post('/login')
                    access_token = response.json['access_token']
                    response = app.post('/player_team/assign/1/1', headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}, json=mocked_player_team.to_dict())
                    assert response.status_code == 201
                    assert response.text == success