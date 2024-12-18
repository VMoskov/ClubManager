import pytest
from app import create_app
from flask import jsonify
from flask_jwt_extended import create_access_token

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True

    @app.route('/login', methods=['POST'])
    def login():
        access_token = create_access_token(identity='1', additional_claims={'email': 'admin@admin.com', 'role': 'admin'})
        return jsonify(access_token=access_token)

    yield app.test_client()