from flask_restful import Resource
from app import api

class Hello(Resource):
    def get(self):
        return 'Hello Rest!'

api.add_resource(Hello, '/api')