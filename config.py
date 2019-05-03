import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'i-love-nastya'

firebase_config = {
    'apiKey': "AIzaSyCd3t3pLFcNtGfnJRpdCwZKOPlcUi3Kbrk",
    'authDomain': "image-rescale.firebaseapp.com",
    'databaseURL': "https://image-rescale.firebaseio.com",
    'projectId': "image-rescale",
    'storageBucket': "image-rescale.appspot.com",
    'messagingSenderId': "85340359287"
  }