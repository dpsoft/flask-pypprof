"""
Expose blueprint function from routes.py or noop_routes.py in case of ImportError(not supported os)
"""
try:
    from flask_pypprof.routes import get_pprof_endpoint_blueprint as blueprint
except ImportError:
    from flask_pypprof.noop_routes import get_noop_pprof_endpoint_blueprint as blueprint

get_pprof_blueprint = blueprint