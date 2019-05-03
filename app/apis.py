import flask
from flask_restful import Resource, reqparse
from flask import request, redirect, flash, render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from urllib.request import urlopen

from app import api, firebase, utils

import os

class ImageUploadAPI(Resource):

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=FileStorage, location='files')
        args = parse.parse_args()
        image_file = args['file']
        file_name = secure_filename(image_file.filename)
        image_file.save(file_name)
        storage = firebase.storage()
        storage.child('images/' + file_name).put(file_name)
        with urlopen(utils.KOTIK_URL, 'r') as f:
            response = flask.make_response(f)
        response.header.set('Content-Type', 'image/jpeg')
        return response

class Hello(Resource):
    def get(self):
        return 'Hello Rest!'

class ImageView(Resource):
    def get(self, fname):
        return render_template('image_view.html', {'file_name': secure_filename(fname)})

api.add_resource(Hello, '/api')
api.add_resource(ImageView, '/image/<string:fname>')
api.add_resource(ImageUploadAPI, '/uploads')