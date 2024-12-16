export SECRET_KEY="your secret key"
export DATABASE_URI="postgresql://admin:admin@localhost:5433/clubmanager"
export JWT_SECRET_KEY="your jwt secret key"

export FLASK_APP=app
export FLASK_ENV=development 
flask db upgrade
flask run