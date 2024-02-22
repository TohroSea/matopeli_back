from flask import Flask
from flask_cors import CORS

from models import db
from api import api


app = Flask(__name__)
CORS(app)
app.config.from_object("config")
db.init_app(app)
with app.app_context():
	db.create_all()
app.register_blueprint(api, url_prefix="/api")
