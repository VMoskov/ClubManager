from app.extensions import db
from app.user.user import User
from app.role.role import Role
from flask_jwt_extended import create_access_token


class UserService:
    def add(self, user):
        if not self.is_valid(user):
            raise ValueError('Invalid user')
        
        user = User(name=user['name'], surname=user['surname'], email=user['email'], password=user['password'])
        if self.already_exists(user):
            raise ValueError('User already exists')
        
        db.session.add(user)
        db.session.commit()
        return user
    
    def get(self, id=None):
        if id is None:
            return User.query.all()
        return User.query.get(id)
    
    def get_roles(self, id):
        user = User.query.get(id)
        if user is None:
            return None
        
        roles = user.roles
        return [role.to_dict() for role in roles]
    
    def assign_role(self, user_id, role_id):
        user = User.query.get(user_id)
        if user is None:
            return None
        
        role = Role.query.get(role_id)
        if role is None:
            return None
        
        user.roles.append(role)
        db.session.commit()
        return user
    
    def delete_role(self, user_id, role_id):
        user = User.query.get(user_id)
        if user is None:
            return None
        
        role = Role.query.get(role_id)
        if role is None:
            return None
        
        user.roles.remove(role)
        db.session.commit()
        return user
    
    def update(self, id, user):
        if not self.is_valid(user):
            raise ValueError('Invalid user')
        
        user_to_update = User.query.get(id)
        if user_to_update is None:
            return None
        
        user_to_update.name = user['name']
        user_to_update.surname = user['surname']
        user_to_update.email = user['email']
        user_to_update.password = user['password']
        if self.already_exists(user_to_update):
            raise ValueError('User already exists')
        
        db.session.commit()
        return user_to_update
    
    def delete(self, id):
        user = User.query.get(id)
        if user is None:
            return None
        
        db.session.delete(user)
        db.session.commit()
        return user
    
    def authenticate(self, email, password):
        user = User.query.filter_by(email=email).first()
        if user is None:
            return None
        
        if user.password != password:
            return None
        
        access_token = create_access_token(identity=user.id, additional_claims={'email': user.email, 'roles': [role.name for role in user.roles]})
        return access_token
    
    def is_valid(self, user):
        return 'name' in user and 'surname' in user and 'email' in user and 'password' in user
    
    def already_exists(self, user):
        return User.query.filter_by(email=user.email).first() is not None