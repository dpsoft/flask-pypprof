from flask_pypprof import get_pprof_blueprint
from flask import Flask


def test_pprof_endpoints():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(get_pprof_blueprint())

    with flask_app.test_client() as test_client:
        response = test_client.get('/debug/pprof/profile?seconds=1')
        assert response.status_code == 200

        response = test_client.get('/debug/pprof/thread')
        assert response.status_code == 200

        response = test_client.get('/debug/pprof/goroutine')
        assert response.status_code == 200

        response = test_client.get('/debug/pprof/heap')
        assert response.status_code == 200

        # disable wall profiling, the process with exit code 142 (interrupted by signal 14: SIGALRM)
        # response = test_client.get('/debug/pprof/wall')
        # assert response.status_code == 200

