from unittest.mock import MagicMock, patch


def test_get_all_players_route(app):
    mocked_players = [
        MagicMock(id=1, name='John Doe', birth_date='1990-01-01', dominant_foot='R', to_dict=lambda: {
            'id': 1,
            'name': 'John Doe',
            'birth_date': '1990-01-01',
            'dominant_foot': 'R'
        }),
        MagicMock(id=2, name='Jane Doe', birth_date='1995-01-01', dominant_foot='L', to_dict=lambda: {
            'id': 2,
            'name': 'Jane Doe',
            'birth_date': '1995-01-01',
            'dominant_foot': 'L'
        })
    ]

    with patch('app.player.service.PlayerService.get', return_value=mocked_players):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.get('/player/', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json == [player.to_dict() for player in mocked_players]


def test_get_player_by_id_route(app):
    mocked_player = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', dominant_foot='R', to_dict=lambda: {
        'id': 1,
        'name': 'John Doe',
        'birth_date': '1990-01-01',
        'dominant_foot': 'R'
    })

    with patch('app.player.service.PlayerService.get', return_value=mocked_player):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.get('/player/1', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json == mocked_player.to_dict()


def test_add_player_route(app):
    success = 'Player added'
    mocked_player = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', dominant_foot='R', to_dict=lambda: {
        'id': 1,
        'name': 'John Doe',
        'birth_date': '1990-01-01',
        'dominant_foot': 'R'
    })

    with patch('app.player.service.PlayerService.add', return_value=mocked_player):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.post('/player/add', headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}, json=mocked_player.to_dict())
        
        assert response.status_code == 201
        assert response.text == success


def test_update_player_route(app):
    success = 'Player updated'
    mocked_player = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', position='GK', to_dict=lambda: {
        'id': 1,
        'name': 'John Doe',
        'birth_date': '1990-01-01',
        'dominant_foot': 'R'
    })

    with patch('app.player.service.PlayerService.update', return_value=mocked_player):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.put('/player/update/1', headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}, json=mocked_player.to_dict())
       
        assert response.status_code == 200
        assert response.text == success


def test_delete_player_route(app):
    success = 'Player deleted'
    with patch('app.player.service.PlayerService.delete', return_value=success):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.delete('/player/delete/1', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.text == success