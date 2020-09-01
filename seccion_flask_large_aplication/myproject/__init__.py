from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/victoria/desarrollo/flask/seccion_flask_large_aplication/myproject/data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)

# Conecta la aplicación con la BD
Migrate(app, db)

# Para poder utilizar los Blueprints necesitamos que la bd este configurada primero
# Importamos las vistas y registramos 
from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')