from flask import Flask
from config import Config, firebase_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
import pyrebase

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
cors = CORS(app, resources={r'/*': {'origins': '*'}})


firebase = pyrebase.initialize_app(firebase_config)



from app import routes, models, apis, utils

