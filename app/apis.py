from flask_restful import Resource, reqparse
from flask import request, redirect, flash, render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from app import api, firebase

import os

class ImageUploadAPI(Resource):

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=FileStorage, location='files')
        args = parse.parse_args()
        image_file = args['file']
        file_name = secure_filename(image_file.filename)
        path_to_file = os.path.join(os.path.dirname(__file__), 'images', file_name)
        image_file.save(path_to_file)
        storage = firebase.storage()
        storage.child('images/' + file_name).put(path_to_file)


class Hello(Resource):
    def get(self):
        return 'Hello Rest!'

class ImageView(Resource):
    def get(self, fname):
        return render_template('image_view.html', {'file_name': secure_filename(fname)})

api.add_resource(Hello, '/api')
api.add_resource(ImageView, '/image/<string:fname>')
api.add_resource(ImageUploadAPI, '/uploads')