# Creamos entradas a la BD

from models import db, Puppy, Owner, Toy

# Creamos dos puppies

rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Agregamos los puppies a la bd
db.session.add_all([rufus, fido])
db.session.commit()

# Verificamos
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name = 'Rufus').first()
print(rufus)

# Creamos un Owner
jose = Owner('Jose', rufus.id)

# Creamos algunos Toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

rufus = Puppy.query.filter_by(name = 'Rufus').first()
print(rufus)

rufus.report_toys()