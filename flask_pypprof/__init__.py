"""
Expose blueprint function
"""
from flask_pypprof.routes import get_pprof_endpoint_blueprint as blueprint

get_pprof_blueprint = blueprint