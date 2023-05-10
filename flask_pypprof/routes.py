import mprofile
from flask import Blueprint, Response, request

from flask_pypprof.handler import ProfileRequestHandler


def get_pprof_endpoint_blueprint() -> Blueprint:
    """Handle pprof endpoint requests a la Go's net/http/pprof.

        The following endpoints are implemented:
          - /debug/pprof/profile: Collect a CPU profile.
          - /debug/pprof/wall: Collect a wall-clock profile.
          - /debug/pprof/heap: Get snapshot of current heap profile.
          - /debug/pprof/thread (or /debug/pprof/goroutine): Currently running threads.
    """

    blueprint = Blueprint("flask-pypprof", __name__, url_prefix="/debug/pprof")

    @blueprint.route('/profile', methods=['GET'])
    def profile() -> Response:
        """Get the CPU profile"""
        handler = ProfileRequestHandler(request)
        handler.profile()
        return Response(handler.get_response())

    @blueprint.route('/wall', methods=['GET'])
    def wall() -> Response:
        """Get the Wall profile"""
        handler = ProfileRequestHandler(request)
        handler.wall()
        return Response(handler.get_response())

    @blueprint.route('/heap', methods=['GET'])
    def heap() -> Response:
        """Get the Heap profile"""
        handler = ProfileRequestHandler(request)
        handler.heap()
        return Response(handler.get_response())

    @blueprint.route('/thread', methods=['GET'])
    @blueprint.route('/goroutine', methods=['GET'])
    def thread() -> Response:
        """Get the Thread profile"""
        handler = ProfileRequestHandler(request)
        handler.thread()
        return Response(handler.get_response())

    @blueprint.record
    def record_params(setup_state):
        app = setup_state.app
        # Start the profiler with the given sample rate or the default value
        mprofile.start(sample_rate=getattr(app.config, "MEMORY_SAMPLE_RATE", 128 * 1024))

    return blueprint
