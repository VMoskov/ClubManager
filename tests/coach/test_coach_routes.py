from unittest.mock import MagicMock, patch


def test_get_all_coaches_route(app):

    mocked_coaches = [
        MagicMock(id=1, name='John Doe', birth_date='1990-01-01', years_of_experience=5, to_dict=lambda: {
            'id': 1, 
            'name': 'John Doe', 
            'birth_date': '1990-01-01', 
            'years_of_experience': 5
            }),
        MagicMock(id=2, name='Jane Doe', birth_date='1995-01-01', years_of_experience=3, to_dict=lambda: {
            'id': 2, 
            'name': 'Jane Doe', 
            'birth_date': '1995-01-01', 
            'years_of_experience': 3
            })
    ]

    with patch('app.coach.service.CoachService.get', return_value=mocked_coaches):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.get('/coach/', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json == [coach.to_dict() for coach in mocked_coaches]


def test_get_coach_by_id_route(app):
    mocked_coach = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', years_of_experience=5, to_dict=lambda: {
        'id': 1, 
        'name': 'John Doe', 
        'birth_date': '1990-01-01', 
        'years_of_experience': 5
        })

    with patch('app.coach.service.CoachService.get', return_value=mocked_coach):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.get('/coach/1', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json == mocked_coach.to_dict()


def test_add_coach_route(app):
    success = 'Coach added'
    mocked_coach = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', years_of_experience=5, to_dict=lambda: {
        'id': 1,
        'name': 'John Doe',
        'birth_date': '1990-01-01',
        'years_of_experience': 5
        })

    with patch('app.coach.service.CoachService.add', return_value=success):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.post('/coach/add', headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}, json=mocked_coach.to_dict())

        assert response.status_code == 201
        assert response.text == success


def test_update_coach_route(app):
    success = 'Coach updated'
    mocked_coach = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', years_of_experience=5, to_dict=lambda: {
        'id': 1, 
        'name': 'John Doe', 
        'birth_date': '1990-01-01', 
        'years_of_experience': 5
        })

    with patch('app.coach.service.CoachService.update', return_value=mocked_coach):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.put('/coach/update/1', headers={'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}, json=mocked_coach.to_dict())

        assert response.status_code == 200
        assert response.text == success


def test_delete_coach_route(app):
    success = 'Coach deleted'

    with patch('app.coach.service.CoachService.delete', return_value=success):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.delete('/coach/delete/1', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.text == success