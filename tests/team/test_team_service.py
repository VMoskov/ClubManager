from unittest.mock import MagicMock, patch
from app.team.service import TeamService


def test_get_all_teams():
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
            teams = TeamService().get()
            assert teams == mocked_teams


def test_get_team_by_id():
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
            team = TeamService().get(1)
            assert team == mocked_team


def test_add_team():
    mocked_team = MagicMock(id=1, name='Team A', home_station='Stadium A', to_dict=lambda: {
        'id': 1,
        'team_name': 'Team A',
        'home_station': 'Stadium A'
    })

    with patch('app.team.service.TeamService.add', return_value=mocked_team):
        team = TeamService().add(team=mocked_team)
        assert team == mocked_team


def test_get_players():
    mocked_players = [
        MagicMock(id=1, name='John Doe', surname='Doe', to_dict=lambda: {
            'id': 1,
            'name': 'John Doe',
            'surname': 'Doe',
            'birth_date': '1990-01-01',
            'dominant_foot': 'R'
        }),
        MagicMock(id=2, name='Jane Doe', surname='Doe', to_dict=lambda: {
            'id': 2,
            'name': 'Jane Doe',
            'surname': 'Doe',
            'birth_date': '1995-01-01',
            'dominant_foot': 'L'
        })
    ]
    
    with patch('app.team.service.TeamService.get_players', return_value=mocked_players):
        players = TeamService().get_players(id=1)
        assert players == mocked_players


def test_get_players_by_position():
    mocked_players = [
        MagicMock(id=1, name='John Doe', surname='Doe', to_dict=lambda: {
            'id': 1,
            'name': 'John Doe',
            'surname': 'Doe',
            'birth_date': '1990-01-01',
            'dominant_foot': 'R'
        }),
        MagicMock(id=2, name='Jane Doe', surname='Doe', to_dict=lambda: {
            'id': 2,
            'name': 'Jane Doe',
            'surname': 'Doe',
            'birth_date': '1995-01-01',
            'dominant_foot': 'L'
        })
    ]
    
    with patch('app.team.service.TeamService.get_players_by_position', return_value=mocked_players):
        players = TeamService().get_players_by_position(team_id=1, position_id=1)
        assert players == mocked_players


def test_get_home_stadium():
    mocked_home_stadium = MagicMock(id=1, team_name='Team A', home_station='Stadium A', to_dict=lambda: {
        'id': 1,
        'team_name': 'Team A',
        'home_station': 'Stadium A'
    })

    with patch('app.team.service.TeamService.get_home_stadium', return_value=mocked_home_stadium):
        home_stadium = TeamService().get_home_stadium(team_id=1)
        assert home_stadium == mocked_home_stadium


def test_assign_coach():
    mocked_coach_id = 1
    mocked_team_id = 1
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

    with patch('app.team.service.TeamService.assign_coach', return_value=mocked_team):
        with patch('app.coach.service.CoachService.get', return_value=mocked_coach):
            team = TeamService().assign_coach(team_id=mocked_team_id, coach_id=mocked_coach_id)
            assert team == mocked_team


def test_get_coach():
    mocked_coach = MagicMock(id=1, name='John', surname='Doe', to_dict=lambda: {
        'id': 1,
        'name': 'John',
        'surname': 'Doe',
        'birth_date': '1990-01-01',
        'years_of_experience': 10
    })

    with patch('app.team.service.TeamService.get_coach', return_value=mocked_coach):
        coach = TeamService().get_coach(id=1)
        assert coach == mocked_coach


def test_delete_coach():
    success = 'Coach deleted'
    mocked_team_id = 1
    with patch('app.team.service.TeamService.delete_coach', return_value=success):
        response = TeamService().delete_coach(id=mocked_team_id)
        assert response == success


def test_delete_team():
    success = 'Team deleted'
    mocked_team_id = 1
    with patch('app.team.service.TeamService.delete', return_value=success):
        response = TeamService().delete(id=mocked_team_id)
        assert response == success


def test_update_team():
    mocked_team_id = 1
    mocked_team = MagicMock(id=mocked_team_id, name='Team A', home_station='Stadium A', to_dict=lambda: {
        'id': 1,
        'team_name': 'Team A',
        'home_station': 'Stadium A'
    })

    with patch('app.team.service.TeamService.update', return_value=mocked_team):
        team = TeamService().update(id=mocked_team_id, team=mocked_team)
        assert team == mocked_team