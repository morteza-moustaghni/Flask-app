from flask.ext.wtf import Form, TextField, TextAreaField, DateTimeField, PasswordField
from wtforms.validators import InputRequired, Email

class ExampleForm(Form):
	title = TextField(u'Title', validators = [InputRequired()])
	content = TextAreaField(u'content')
	date = DateTimeField(u'Date', format='%d/%m/%Y %H:%M')
	#recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(Form):
	user = TextField(u'Username', validators = [InputRequired()])
	password = PasswordField(u'Password', validators = [InputRequired()])

class NewAccountForm(Form):
	email = EmailField(u'Email', validators = [InputRequired(), Email()])
	user = TextField(u'Username', validators = [InputRequired()])
	password = PasswordField(u'Password', validators = [InputRequired()])