from flask_pypprof import get_pprof_blueprint
from flask import Flask


def test_pprof_endpoints():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(get_pprof_blueprint())

    with flask_app.test_client() as test_client:
        response = test_client.get('/debug/pprof/profile?seconds=1')
        assert response.status_code == 200
