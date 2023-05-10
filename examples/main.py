import sys

from flask import Flask
from flask_restful import Resource, Api

from flask_pypprof import get_pprof_blueprint


class Hello(Resource):
    @staticmethod
    def get():
        return {'hello': 'world world'}


app = Flask(__name__)
app.register_blueprint(get_pprof_blueprint())

api = Api(app)
api.add_resource(Hello, '/')

port = 5100

if sys.argv.__len__() > 1:
    port = sys.argv[1]

print("Api running on port : {} ".format(port))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
