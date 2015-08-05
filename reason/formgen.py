
### Form generation - Form Templates

from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from flask.ext.wtf.html5 import URLField, EmailField
from wtforms.validators import DataRequired
from werkzeug import secure_filename
from flask_wtf.file import FileField, FileAllowed
from wtforms import validators, ValidationError, SubmitField
from werkzeug import secure_filename
from wtforms.fields.html5 import URLField
from wtforms import SelectField
from wtforms.validators import url, DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from models import User


#Form for uploading Pom.xml or Jar File for scanning
class pomxmlForm(Form):
    pomxml = FileField('pomxml', validators=[DataRequired(), FileAllowed(['xml', 'jar'], 'xml & jars only!')])
    description = StringField('description', validators=[DataRequired(), Length(5,30), Regexp(r'^[A-Za-z0-9:_-]',message=r"Describe with characters [a-z] [A-Z] [0-9] [:_-]")])
	  
   	
#Search Form
class searchForm(Form):
    searchCont = StringField('Seach for :', validators=[DataRequired(), Length(3, 100) ])
    actions = SelectField('Look up for : ', choices=[('cpe', 'cpe'), ('cve', 'cve'), ('cwe', 'cwe'), ('exp', 'exploit') ])
    startSearch = SubmitField('Search')


#Login Form 
class LoginForm(Form):
    username = StringField('Username:', validators=[DataRequired(), Length(3,80), Regexp(r'^[A-Za-z0-9_]{3,}$')])
    password = PasswordField('Password', validators=[DataRequired(), Length(3,30), Regexp(r'^[0-9A-Za-z_$@]{3,}$')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class SignupForm(Form):
    username = StringField('Username',
                    validators=[
                        DataRequired(), Length(3, 80),
                        Regexp(r'^[A-Za-z0-9_]{3,}$',
                            message='Usernames consist of numbers, letters,'
                                    'and underscores.')])
    password = PasswordField('Password',
                    validators=[
                        DataRequired(), Length(8, 30), Regexp(r'^[A-Za-z0-9_$@]{8,}$', message=r'Password can be 8-30 characters long, [A-Z] [a-z] [0-9] [-_$@] are alowed'),
                        EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Length(5, 120), Email()])
    

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('There already is a user with this email address.')

    def validate_username(self, username_field):
       if User.query.filter_by(username=username_field.data).first():
           raise ValidationError('This username is already taken, try something else!')

