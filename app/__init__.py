from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from app.config import Config

app = Flask(__name__, static_url_path='/static')

app.config.from_object(Config)

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
Bootstrap(app)

from app import views
