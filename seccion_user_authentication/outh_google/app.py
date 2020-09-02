import os
os.environ['OUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

blueprint = make_google_blueprint(client_id='573489112383-5olgvb03n9u9efl4162e8m21iu2uhm4n.apps.googleusercontent.com', client_secret='mU6-3vy2C0HNeosRacGhz7r_', offline=True, scope=['profile', 'email'])

app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/welcome')
def welcome():
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email=resp.json()["email"]

    return render_template("welcome.html",email=email)

@app.route('/login/google')
def login():
	"""
	Esta funcion nos permite utilizar el servicio de autenticacion
	de Google para poder ingresar a nuestro sitio.
	"""
	if not google.authorized:
		return render_template(url_for('google.log'))
	resp = google.get('/outh2/v2/userinfo')
	assert resp.ok, resp.text
	email = resp.json()['email']
	return render_template('welcome.hmtl', email=email)

if __name__ == '__main__':
	app.run()