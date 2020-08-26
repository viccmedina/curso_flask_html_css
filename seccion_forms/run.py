from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

"""
Configuramos una clave secreta para
poder deployar y usarla en los formularios.
Por ahora no será muy sofisticada
"""

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
	"""
	Clase que genera el formulario
	que toma información general 
	sobre puppies.
	Heredamos de FlaskForm.
	"""

	breed = StringField('What Breed are you?')
	submit = SubmitField('Submit')


# Declaramos una ruta donde especificamos
# los métodos HTTP que aceptará
@app.route('/', methods=['GET', 'POST'])
def index():
	# será usada en el html
	breed = False
	# creamos una instancia del formulario
	form = InfoForm()
	# validamos el formulario en base a lo declarado
	# en la clase InfoForm
	if form.validate_on_submit():
		breed = form.breed.data
		form.breed.data = ''
	return render_template('index.html', form=form, breed=breed)

if __name__ == '__main__':
	app.run(debug=True)