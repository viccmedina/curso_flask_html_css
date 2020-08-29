import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Recuperamos el path absoluto de donde esta 
# nuestro archivo para la bd
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Puppy(db.Model):

    # Nombre de la tabla, si no lo seteamos tomara el nombre
    # de la clase
    __tablename__ = 'puppies'

    #####################################
    ## CREATE THE COLUMNS FOR THE TABLE #
    #####################################

    # Primary Key column, unique id for each puppy
    id = db.Column(db.Integer,primary_key=True)
    # Puppy name
    name = db.Column(db.Text)
    # Puppy age in years
    age = db.Column(db.Integer)

    # This sets what an instance in this table will have
    # Note the id will be auto-created for us later, so we don't add it here!
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        # This is the string representation of a puppy in the model
        return f"Puppy {self.name} is {self.age} years old."