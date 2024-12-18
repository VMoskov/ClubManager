from unittest.mock import MagicMock, patch
from app.position.service import PositionService


def test_get_all_positions():
    mocked_positions = [
        MagicMock(id=1, name='Position 1'),
        MagicMock(id=2, name='Position 2'),
        MagicMock(id=3, name='Position 3')
    ]

    with patch('app.position.service.PositionService.get', return_value=mocked_positions):
        positions = PositionService().get()
        assert positions == mocked_positions