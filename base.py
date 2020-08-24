from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1> Hello Puppy! </h1>'

@app.route('/information')
def information():
	return '<h1> Puppies are cute! </h1>'

"""
URL dinámicas
"""
@app.route('/puppy/<name>')
def puppy(name):
	return 'You said: {}'.format(name)

if __name__ == '__main__':
	app.run(debug=True)