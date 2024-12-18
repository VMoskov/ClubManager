from unittest.mock import MagicMock, patch
from flask import jsonify


def test_get_all_teams_route(app):
    mocked_coaches = [
        MagicMock(id=1, name='John', surname='Doe', to_dict=lambda: {
            'id': 1,
            'name': 'John',
            'surname': 'Doe',
            'birth_date': '1990-01-01',
            'years_of_experience': 10
            }),
        MagicMock(id=2, name='Jane', surname='Doe', to_dict=lambda: {
            'id': 2,
            'name': 'Jane',
            'surname': 'Doe',
            'birth_date': '1995-01-01',
            'years_of_experience': 5
        })
    ]
    mocked_teams = [
        MagicMock(id=1, name='Team A', home_station='Stadium A', coach=mocked_coaches[0], to_dict=lambda: {
            'id': 1,
            'team_name': 'Team A',
            'home_station': 'Stadium A',
            'coach': 'John Doe'
        }),
        MagicMock(id=2, name='Team B', home_station='Stadium B', coach=mocked_coaches[1], to_dict=lambda: {
            'id': 2,
            'team_name': 'Team B',
            'home_station': 'Stadium B',
            'coach': 'Jane Doe'
        })
    ]

    with patch('app.team.service.TeamService.get', return_value=mocked_teams):
        with patch('app.coach.service.CoachService.get', return_value=mocked_coaches):
            response = app.post('/login')
            access_token = response.json['access_token']
            response = app.get('/team/', headers={'Authorization': f'Bearer {access_token}'})

            assert response.status_code == 200
            assert response.json == [team.to_dict() for team in mocked_teams]


def test_get_team_by_id_route(app):
    mocked_coach = MagicMock(id=1, name='John', surname='Doe', to_dict=lambda: {
        'id': 1,
        'name': 'John',
        'surname': 'Doe',
        'birth_date': '1990-01-01',
        'years_of_experience': 10
    })
    mocked_team = MagicMock(id=1, name='Team A', home_station='Stadium A', coach=mocked_coach, to_dict=lambda: {
        'id': 1,
        'team_name': 'Team A',
        'home_station': 'Stadium A',
        'coach': 'John Doe'
    })

    with patch('app.team.service.TeamService.get', return_value=mocked_team):
        with patch('app.coach.service.CoachService.get', return_value=mocked_coach):
            response = app.post('/login')
            access_token = response.json['access_token']
            response = app.get('/team/1', headers={'Authorization': f'Bearer {access_token}'})

            assert response.status_code == 200
            assert response.json == mocked_team.to_dict()


def test_add_team_route(app):
    success = 'Team added'
    mocked_team = MagicMock(id=1, name='Team A', home_station='Stadium A', to_dict=lambda: {
        'id': 1,
        'team_name': 'Team A',
        'home_station': 'Stadium A',
        'coach': 'John Doe'
    })

    with patch('app.team.service.TeamService.add', return_value=mocked_team):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.post('/team/add', headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}, json=mocked_team.to_dict())

        assert response.status_code == 201
        assert response.text == success


def test_get_players_route(app):
    mocked_players = [
        MagicMock(id=1, name='John Doe', surname='Doe', to_dict=lambda: {
            'id': 1,
            'name': 'John Doe',
            'surname': 'Doe'
        }),
        MagicMock(id=2, name='Jane Doe', surname='Doe', to_dict=lambda: {
            'id': 2,
            'name': 'Jane Doe',
            'surname': 'Doe'
        })
    ]

    with patch('app.team.service.TeamService.get_players', return_value=mocked_players):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.get('/team/1/players', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json == [player.to_dict() for player in mocked_players]


def test_get_players_by_position_route(app):
    mocked_players = [
        MagicMock(id=1, name='John Doe', surname='Doe', to_dict=lambda: {
            'id': 1,
            'name': 'John Doe',
            'surname': 'Doe'
        }),
        MagicMock(id=2, name='Jane Doe', surname='Doe', to_dict=lambda: {
            'id': 2,
            'name': 'Jane Doe',
            'surname': 'Doe'
        })
    ]

    with patch('app.team.service.TeamService.get_players_by_position', return_value=mocked_players):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.get('/team/1/players/1', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json == [player.to_dict() for player in mocked_players]


def test_get_home_stadium_route(app):
    mocked_home_stadium = MagicMock(id=1, name='Team A', home_stadium='Stadium A', to_dict=lambda: {
        'id': 1,
        'team': 'Team A',
        'home_stadium': 'Stadium A'
    })

    with patch('app.team.service.TeamService.get_home_stadium', return_value=mocked_home_stadium):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.get('/team/1/home_stadium', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json == mocked_home_stadium.to_dict()


def test_assign_coach_route(app):
    success = 'Coach assigned'

    with patch('app.team.service.TeamService.assign_coach', return_value=True):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.put('/team/1/assign_coach/1', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.text == success


def test_get_coach_route(app):
    mocked_coach = MagicMock(id=1, name='John', surname='Doe', to_dict=lambda: {
        'id': 1,
        'name': 'John',
        'surname': 'Doe',
        'birth_date': '1990-01-01',
        'years_of_experience': 10
    })

    with patch('app.team.service.TeamService.get_coach', return_value=mocked_coach):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.get('/team/1/coach', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json == mocked_coach.to_dict()


def test_delete_coach_route(app):
    success = 'Coach deleted'

    with patch('app.team.service.TeamService.delete_coach', return_value=True):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.delete('/team/1/delete_coach', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.text == success
                              

def test_update_team_route(app):
    success = 'Team updated'
    mocked_team = MagicMock(id=1, name='Team A', home_station='Stadium A', to_dict=lambda: {
        'id': 1,
        'team_name': 'Team A',
        'home_station': 'Stadium A',
        'coach': 'John Doe'
    })

    with patch('app.team.service.TeamService.update', return_value=True):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.put('/team/1/update', headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}, json=mocked_team.to_dict())

        assert response.status_code == 200
        assert response.text == success


def test_delete_team_route(app):
    success = 'Team deleted'

    with patch('app.team.service.TeamService.delete', return_value=True):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.delete('/team/1/delete', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.text == success