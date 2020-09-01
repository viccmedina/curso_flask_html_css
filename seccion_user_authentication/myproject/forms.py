from flask import FaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log in')


class  RegistrationForm(FaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', 
		message='Passwords must match!')])
	pass_confirm = PasswordField('Confirm Password', validators[DataRequired()])


	def check_email(self, field):
		"""
		Si el email pasado como parametro no esta dentro de la BD,
		es aceptado, caso contrario se lanza una excepion.
		"""
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Your email has been already registered!')

	def check_username(self, field):
		"""
		Realizamos la verificación sobre el username.
		Si el mismo ya existe en la db, lanzamos una excepción.
		"""

		if User.query.filter_by(username=field.data).first():
			raise ValidationError('The username is already in use!')
