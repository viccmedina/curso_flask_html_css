from flask_wtf impor FormFlask
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class BlogPostForm(FormFlask):
	title = StringField('Title', validators=[DataRequired()])
	text = StringField('Text', validators=[DataRequired()])
	submit = SubmitField('Post')