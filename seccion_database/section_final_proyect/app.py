from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm , DelForm, AddFormOwner

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecrectkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/vmedina/UNLu/curso_flask_html_css/seccion_database/section_final_proyect/data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Conecta la aplicación con la BD
Migrate(app, db)

class Puppy(db.Model):
	# Nombre de la tabla
	__tablename__ = 'puppies'
	
	# Clave Primaria
	id = db.Column(db.Integer, primary_key = True)

	# Atributo nombre
	name = db.Column(db.Text)

	# Atributo que relaciona un puppy con un owner
	owner = db.relationship('Owner', backref='puppy', uselist=False)

	# Constructor
	def __init__(self, name):
		self.name = name

	# Representación en texto
	def __repr__(self):
		if self.owner:
			return f"Puppy name is {self.name} and the owner is {self.owner.name}"
		else:
			return f"Puppy name is {self.name} and has no owner yet!"


class Owner(db.Model):
	__tablename__ = 'owners'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text)

	puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

	def __init__(self, name, puppy_id):
		self.name = name
		self.puppy_id = puppy_id

	def __repr__(self):
		return f"The owner is {self.name}"


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

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
	form = AddFormOwner()
	if form.validate_on_submit():
		pup_id = form.id.data
		name = form.name.data
		new_owner = Owner(name, pup_id)
		db.session.add(new_owner)
		db.session.commit()
		return redirect(url_for('list_pup'))
	return render_template('add_owner.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)