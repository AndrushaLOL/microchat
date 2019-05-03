from flask import Flask
from config import Config, firebase_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
import pyrebase

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

firebase = pyrebase.initialize_app(firebase_config)



from app import routes, models, apis
