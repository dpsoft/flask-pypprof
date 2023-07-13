"""
Expose blueprint function
"""
from flask_pypprof.routes import get_pprof_endpoint_blueprint as blueprint

get_pprof_blueprint = blueprint

# Version of the flask_pypprof package
__version__ = "0.1.0"