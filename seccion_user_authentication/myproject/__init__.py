from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/victoria/desarrollo/flask/seccion_user_authentication/myproject/data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'login'