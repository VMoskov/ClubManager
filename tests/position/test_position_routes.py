from unittest.mock import MagicMock, patch


def test_get_all_positions_route(app):
    mocked_positions = [
        MagicMock(id=1, name='Position 1', to_dict=lambda: {'id': 1, 'name': 'Position 1'}),
        MagicMock(id=2, name='Position 2', to_dict=lambda: {'id': 2, 'name': 'Position 2'}),
        MagicMock(id=3, name='Position 3', to_dict=lambda: {'id': 3, 'name': 'Position 3'})
    ]

    with patch('app.position.service.PositionService.get', return_value=mocked_positions):
        response = app.post('/login')
        access_token = response.json['access_token']
        response = app.get('/position/', headers={'Authorization': f'Bearer {access_token}'})

        assert response.status_code == 200
        assert response.json == [position.to_dict() for position in mocked_positions]