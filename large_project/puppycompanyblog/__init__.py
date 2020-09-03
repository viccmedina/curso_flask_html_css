from flask import Flask
from flask_alchemy import SQALchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# Data Base
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:////home/victoria/desarrollo/flask/large_project/puppycompanyblog/data.sqlite'
app.config = ['SQALCHEMY_TRACK_MODIFICATIONS'] = False
Migrate(app, db)

# Login Config
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


# Blueprints

from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)