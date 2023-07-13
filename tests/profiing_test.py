# from flask import Flask
# import pytest

# from flask_pypprof import get_pprof_blueprint

from normalize import normalize


def test_spaces():
    number = '555 12 34' # input number
    normalized_number = normalize(number)
    assert normalized_number == '5551234'

# @pytest.fixture(scope='module')
# def client():
#     app = Flask('flask_ping.flask_test_app')
#     app.register_blueprint(get_pprof_blueprint())
#     return app.test_client()
