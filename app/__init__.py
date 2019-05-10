from flask import Flask
from config import Config, firebase_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
import pyrebase
import os
from ISR.models import RDN

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
cors = CORS(app, resources={r'/*': {'origins': '*'}})

rdn = RDN(arch_params={'C': 6, 'D': 20, 'G': 64, 'G0': 64, 'x': 2})
rdn.model.load_weights(os.path.join(os.path.dirname(__file__), 'model_weights/rdn-C6-D20-G64-G064-x2_ArtefactCancelling_epoch219.hdf5'))
rdn.model._make_predict_function()
firebase = pyrebase.initialize_app(firebase_config)



from app import routes, models, apis, utils, forms, predict, rescale

