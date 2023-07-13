from flask_pypprof import get_pprof_blueprint
from flask import Flask
import pytest
import os


@pytest.fixture(scope='module')
def test_pprof_endpoints():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'

    flask_app = Flask('flask_ping.flask_test_app')
    # flask_app.register_blueprint(get_pprof_blueprint())

    with flask_app.test_client() as test_client:
        response = test_client.get('/debug/pprof/profile')
        assert response.status_code == 400
        assert b"Flask User Management Example!" not in response.data
