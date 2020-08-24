from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1> Welcome! Go to /puppy_latin to see \
			your name in puppy latin </h1>'

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
	puppy_latin_name = ''
	if name[len(name) -1 ] == 'y':
		puppy_latin_name = name[:-1] + 'iful'
	else:
		puppy_latin_name = name + 'y'

	return '<h1> Hi {}! Yout puppylatin name is {}</h1>'.format(name, puppy_latin_name)

if __name__ == '__main__':
	app.run(debug=True)