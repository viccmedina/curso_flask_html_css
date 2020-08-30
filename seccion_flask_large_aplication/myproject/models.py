from myproject import db

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