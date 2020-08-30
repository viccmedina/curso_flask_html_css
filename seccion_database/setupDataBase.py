from basic import db, Puppy

# Crea todas las tablas
db.create_all()

sam = Puppy('Sammy', 3, 'Lab')
frank = Puppy('Frankie', 4, 'Shepard')

# Podemos agregarlo a la db con una sola línea
# Para ello, le pasamos por parámetro una lista.

db.session.add_all([sam, frank])

# Guardamos los objetos
db.session.commit()

# Obtenemos todos los elementos de tipo Puppy
# de la tabla puppy

all_puppies = Puppy.query.all()
print(all_puppies)

# Podemos filtrar por una columna de la tabla
# Siempre dará como resultado una lista.

puppy_frankie = Puppy.query.filter_by(name='Frankie')

########## UPDATE

# Recuperamos el primer elemento
first_puppy = Puppy.query.get(1)

first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

###### DELETE

second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)