from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
swagger = Swagger()
jwt = JWTManager()