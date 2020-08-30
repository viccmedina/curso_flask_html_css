from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
	name = StringField('Name of Owner:')
	id = IntegerField('Id Number of Puppy:')
	submit = SubmitField('Add Owner')	


class DelForm(FlaskForm):
	id = IntegerField('Id Number of Puppy to Remove:')
	submit = SubmitField('Remove Puppy')