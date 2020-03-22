from flask.ext.wtf import Form, TextField, TextAreaField, DateTimeField, PasswordField
from flask.ext.wtf import Required
from wtforms import validators
from wtforms.fields.html5 import EmailField

class ExampleForm(Form):
	title = TextField(u'Title', validators = [Required()])
	content = TextAreaField(u'content')
	date = DateTimeField(u'Date', format='%d/%m/%Y %H:%M')
	#recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(Form):
	user = TextField(u'Username', validators = [Required()])
	password = PasswordField(u'Password', validators = [Required()])

class NewAccountForm(Form):
	email = EmailField(u'Email', validators = [validators.DataRequired(), validators.Email()])
	user = TextField(u'Username', validators = [Required()])
	password = PasswordField(u'Password', validators = [Required()])