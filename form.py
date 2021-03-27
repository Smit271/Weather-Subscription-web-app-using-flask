from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# Making RegistrationForm inherited from FlaskForm 
class RegistrationForm(FlaskForm):
	name = StringField('Name',
						validators = [DataRequired()])
	email = StringField('Email',
						validators = [DataRequired(), Email()])
	city = StringField('City',
						validators = [DataRequired()])
	submit = SubmitField('Sign up')

class Weather(FlaskForm):
	city_name = StringField('Search City', validators = [DataRequired()])
	search = SubmitField('Search')