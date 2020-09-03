from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidatonError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from puppycompayblog.models import User


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	username = email = StringField('UserName', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()], EqualTo('pass_confirm', message='Password must match'))
	pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
	submit = SubmitField('Register!')

	def check_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidatonError('Your email has been registrered already!')

	def check_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidatonError('Your username has been registrered already!')


class UpdateUserForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	username = email = StringField('UserName', validators=[DataRequired()])
	picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def check_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidatonError('Your email has been registrered already!')

	def check_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidatonError('Your username has been registrered already!')