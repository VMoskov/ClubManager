from app.extensions import db
from app.player.player import Player


class PlayerService:
    def add(self, player):
        if not self.is_valid(player):
            raise ValueError('Invalid player')
        
        player = Player(name=player['name'], surname=player['surname'], birth_date=player['birth_date'], dominant_foot=player['dominant_foot'])

        if player.surname == 'null':
            player.surname = None

        if player.birth_date == 'null':
            player.birth_date = None

        if self.already_exists(player):
            raise ValueError('Player already exists')
        
        db.session.add(player)
        db.session.commit()
        return player
    
    def get(self, id=None):
        if id is None:
            return Player.query.all()
        return Player.query.get(id)
    
    def update(self, id, new_data):
        player = Player.query.get(id)
        if player is None:
            raise ValueError('Player not found')
        
        if not self.is_valid(new_data):
            raise ValueError('Invalid player data')
        
        player.name = new_data['name'] if new_data['name'] != 'null' else player.name
        player.surname = new_data['surname'] if new_data['surname'] != 'null' else player.surname
        player.birth_date = new_data['birth_date'] if new_data['birth_date'] != 'null' else player.birth_date
        player.dominant_foot = new_data['dominant_foot'] if new_data['dominant_foot'] != 'null' else player.dominant_foot

        db.session.commit()
        return player

    def delete(self, id):
        player = Player.query.get(id)
        if player is None:
            raise ValueError('Player not found')
        
        db.session.delete(player)
        db.session.commit()
    
    def is_valid(self, player):
        if player is None or not all(key in player for key in ['name', 'surname', 'birth_date', 'dominant_foot']):
            return False
        return True
    
    def already_exists(self, player):
        return Player.query.filter_by(name=player.name, surname=player.surname).first() is not None