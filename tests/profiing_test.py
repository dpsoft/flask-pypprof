from flask import Flask
import pytest

from flask_pypprof import get_pprof_blueprint


@pytest.fixture(scope='module')
def client():
    app = Flask('flask_ping.flask_test_app')
    app.register_blueprint(get_pprof_blueprint())
    return app.test_client()
