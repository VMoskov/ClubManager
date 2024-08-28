export SECRET_KEY="your secret key"
export DATABASE_URI="postgresql://admin:admin@localhost:5433/clubmanager"

export FLASK_APP=app
export FLASK_ENV=development 
flask db upgrade
flask run