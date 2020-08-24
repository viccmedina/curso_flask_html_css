from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	name = 'Vicky'
	letters = list(name)
	pup_dictionary = {'pup_name': 'Sammy'}
	puppies_names = [ 'Rufus', 'Spike', 'Boby']
	return render_template('basic.html', name=name, 
		letters=letters, pup_dictionary=pup_dictionary,
		puppies_names=puppies_names)

if __name__ == '__main__':
	app.run(debug=True)