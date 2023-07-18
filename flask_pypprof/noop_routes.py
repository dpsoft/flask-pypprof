import sys

from flask import Blueprint, Response


def get_noop_pprof_endpoint_blueprint() -> Blueprint:
    blueprint = Blueprint("noop-flask-pypprof", __name__, url_prefix="/debug/pprof")
    platform = sys.platform

    @blueprint.route('/profile', methods=['GET'])
    def profile() -> Response:
        """Get the CPU profile"""
        return Response("cpu profiling not supported on this Platform: {}".format(platform))

    @blueprint.route('/wall', methods=['GET'])
    def wall() -> Response:
        """Get the Wall profile"""
        return Response("wall profiling not supported on this Platform: {}".format(platform))

    @blueprint.route('/heap', methods=['GET'])
    def heap() -> Response:
        """Get the Heap profile"""
        return Response("heap profiling not supported on this Platform: {}".format(platform))

    @blueprint.route('/thread', methods=['GET'])
    @blueprint.route('/goroutine', methods=['GET'])
    def thread() -> Response:
        """Get the Thread profile"""
        return Response("thread profiling not supported on this Platform: {}".format(platform))

    return blueprint
