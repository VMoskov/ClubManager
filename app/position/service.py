from app.extensions import db
from app.position.position import Position


class PositionService:
    def add(self, position):
        pass

    def get(self, id=None):
        if id is None:
            return Position.query.all()
        return Position.query.get(id)