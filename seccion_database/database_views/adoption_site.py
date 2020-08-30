from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import  AddForm , DelForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecrectkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/vmedina/UNLu/curso_flask_html_css/seccion_database/database_views/data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Conecta la aplicación con la BD para poder hacer las migraciones
Migrate(app, db)

# Cuando el proyecto es más grande conviene tener los modelos aparte

class Puppy(db.Model):

    # Nombre de la tabla, si no lo seteamos tomara el nombre
    # de la clase
    __tablename__ = 'puppies'

    #####################################
    ## CREATE THE COLUMNS FOR THE TABLE #
    #####################################

    # Primary Key column, unique id for each puppy
    id = db.Column(db.Integer, primary_key=True)
    # Puppy name
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # This is the string representation of a puppy in the model
        return f"Puppy name: {self.name}"

# Vistas

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
	form = AddForm()
	if form.validate_on_submit():
		name = form.name.data
		new_pup = Puppy(name)
		db.session.add(new_pup)
		db.session.commit()
		return redirect(url_for('list_pup'))
	return render_template('add.html', form = form)

@app.route('/list')
def list_pup():
	puppies = Puppy.query.all()
	print(puppies)
	return render_template('list_pup.html', puppies=puppies)

@app.route('/detele', methods=['GET', 'POST'])
def del_pup():
	form = DelForm()
	if form.validate_on_submit():
		id = form.id.data
		pup = Puppy.query.get(id)
		db.session.delete(pup)
		db.session.commit()
		return redirect(url_for('list_pup'))
	return render_template('delete.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)