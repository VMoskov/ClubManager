from unittest.mock import MagicMock, patch
from app.player.service import PlayerService


def test_get_all_players():
    mocked_players = [
        MagicMock(id=1, name='John Doe', birth_date='1990-01-01', position='GK', to_dict=lambda: {
            'id': 1, 
            'name': 'John Doe', 
            'birth_date': '1990-01-01', 
            'dominant_foot': 'R'
            }),
        MagicMock(id=2, name='Jane Doe', birth_date='1995-01-01', position='DF', to_dict=lambda: {
            'id': 2, 
            'name': 'Jane Doe', 
            'birth_date': '1995-01-01', 
            'dominant_foot': 'L'
            })
    ]

    with patch('app.player.service.PlayerService.get', return_value=mocked_players):
        players = PlayerService().get()
        assert players == mocked_players


def test_get_player_by_id():
    mocked_player = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', position='GK', to_dict=lambda: {
        'id': 1, 
        'name': 'John Doe', 
        'birth_date': '1990-01-01', 
        'dominant_foot': 'R'
        })

    with patch('app.player.service.PlayerService.get', return_value=mocked_player):
        player = PlayerService().get(1)
        assert player == mocked_player


def test_add_player():
    mocked_player = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', position='GK', to_dict=lambda: {
        'id': 1,
        'name': 'John Doe',
        'birth_date': '1990-01-01',
        'dominant_foot': 'R'
        })

    with patch('app.player.service.PlayerService.add', return_value=mocked_player):
        player = PlayerService().add(player=mocked_player)
        assert player == mocked_player


def test_update_player():
    mocked_player = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', position='GK', to_dict=lambda: {
        'id': 1,
        'name': 'John Doe',
        'birth_date': '1990-01-01',
        'dominant_foot': 'R'
        })

    with patch('app.player.service.PlayerService.update', return_value=mocked_player):
        player = PlayerService().update(id=1, player=mocked_player)
        assert player == mocked_player


def test_delete_player():
    success = 'Player deleted'
    with patch('app.player.service.PlayerService.delete', return_value=success):
        response = PlayerService().delete(id=1)
        assert response == success