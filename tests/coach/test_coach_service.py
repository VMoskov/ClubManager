from unittest.mock import MagicMock, patch
from app.coach.service import CoachService


def test_get_all_coaches():
    mocked_coaches = [
        MagicMock(id=1, name='John Doe', birth_date='1990-01-01', years_of_experience=5),
        MagicMock(id=2, name='Jane Doe', birth_date='1995-01-01', years_of_experience=3)
    ]

    with patch('app.coach.service.CoachService.get', return_value=mocked_coaches):
        coaches = CoachService().get()
        assert coaches == mocked_coaches


def test_get_coach_by_id():
    mocked_coach = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', years_of_experience=5)

    with patch('app.coach.service.CoachService.get', return_value=mocked_coach):
        coach = CoachService().get(1)
        assert coach == mocked_coach


def test_add_coach():
    mocked_coach = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', years_of_experience=5)

    with patch('app.coach.service.CoachService.add', return_value=mocked_coach):
        coach = CoachService().add(coach=mocked_coach)
        assert coach == mocked_coach


def test_update_coach():
    mocked_coach = MagicMock(id=1, name='John Doe', birth_date='1990-01-01', years_of_experience=5)

    with patch('app.coach.service.CoachService.update', return_value=mocked_coach):
        coach = CoachService().update(id=1, coach=mocked_coach)
        assert coach == mocked_coach


def test_delete_coach():
    success = 'Coach deleted'
    with patch('app.coach.service.CoachService.delete', return_value=success):
        response = CoachService().delete(id=1)
        assert response == success