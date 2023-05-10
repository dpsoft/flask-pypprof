from flask import Blueprint, Response, request

from flask_pypprof.handler import ProfileRequestHandler


def get_profiling_blueprint() -> Blueprint:
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
