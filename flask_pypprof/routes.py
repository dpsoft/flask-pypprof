from django.conf import settings
from django.http import HttpResponse
from pypprof.net_http import PProfRequestHandler

try:
    import mprofile

    has_mprofile = True
except ImportError:
    has_mprofile = False

from flask import Blueprint, Response, request


def get_profiling_blueprint() -> Blueprint:
    settings.configure()
    """Get the blueprint for the profiling routes."""
    blueprint = Blueprint("flask-pypprof", __name__, url_prefix="/debug/pprof")

    @blueprint.route('/profile', methods=['GET'])
    def profile() -> Response:
        """Get the profile"""
        handler = ProfileRequestHandler(request)
        handler.profile()

        return Response(handler.get_response())

    @blueprint.route('/wall', methods=['GET'])
    def wall() -> Response:
        """Get the wall profile."""
        handler = ProfileRequestHandler(request)
        handler.wall()

        return Response(handler.get_response())

    @blueprint.route('/heap', methods=['GET'])
    def heap() -> Response:
        """Get the heap profile."""
        handler = ProfileRequestHandler(request)
        handler.heap()

        return Response(handler.get_response())

    @blueprint.route('/thread', methods=['GET'])
    def thread() -> Response:
        """Get the thread profile."""
        handler = ProfileRequestHandler(request)
        handler.thread()

        return Response(handler.get_response())

    return blueprint


class ProfileRequestHandler(PProfRequestHandler):
    def __init__(self, req):
        self.query = req.args
        self.wfile = HttpResponse()

    def send_response(self, code, message=None):
        self.wfile.status_code = code
        self.wfile.status = message

    def send_error(self, code, message=None, explain=None):
        self.wfile.status_code = code
        self.wfile.status = message

    def send_header(self, keyword, value):
        self.wfile[keyword] = value

    def end_headers(self) -> None:
        pass

    def profile(self):
        super().profile(self.query)

    def wall(self):
        super().wall(self.query)

    def heap(self):
        super().heap(self.query)

    def thread(self):
        super().thread(self.query)

    def get_response(self):
        return self.wfile
