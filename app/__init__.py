from config import Config
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__,static_folder='frontend/build',static_url_path='')
app.config.from_object(Config)
cors = CORS(app)

from app import routes