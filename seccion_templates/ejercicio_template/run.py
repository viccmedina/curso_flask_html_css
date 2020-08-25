from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
	"""
	Pruebo pasando una lista con los requerimientos
	solicitados.
	"""
	restraints = [
		'Must have an upper case letter somewhere.',
		'Must have a lower case letter somewhere.',
		'Must have a number at the end.'
	]
	return render_template('index.html', rrestraints=restraints)

@app.route('/report')
def report():
	"""
	Tomo el valor cargado en el formulario.
	Seteo el título y subtítulo.
	Determino si hay errores.
	"""
	username = request.args.get('username')
	result = check_username(username)
	title = 'Let see how you performed!!'
	if len(result) != 3:
		subtitle = 'Oh no! Looks like you had issues with your username!'
	else:
		subtitle = 'Your username passed the 3 requirements!'
		result = None
	return render_template('report.html', result=result, title=title, subtitle=subtitle)

def check_username(username):
	"""
	Verifica si se cumplen las siguientes retricciones:
	- username debe finalizar en un número.
	- username debe contener al menos una letra minúscula.
	- username debe contener al menos una letra mayúscula.
	"""
	result = list()
	if not (re.findall('[0-9]', username[-1])):
		result.append('Username NOT end in a number')

	if not re.findall('[a-z]', username):
		result.append('Username NOT contained an lowercase letter')

	if not re.findall('[A-Z]', username):
		result.append('Username NOT contained an uppercase letter')
	return result

@app.errorhandler(404)
def page_not_found(e):
	"""
	Mostramos un página por defult si no se encuentra
	la sección deseada.
	"""
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)