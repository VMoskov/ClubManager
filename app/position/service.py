from app.extensions import db
from app.position.position import Position


class PositionService:
    def add(self, position):
        db.session.add(position)
        db.session.commit()
        return position

    def get(self, id=None):
        if id is None:
            return Position.query.all()
        return Position.query.get(id)