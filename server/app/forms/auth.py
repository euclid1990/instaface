from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class AuthForm(object):
    class Register(FlaskForm):
        email = StringField('email', validators=[DataRequired(), Email()])
        password = PasswordField('password', validators=[DataRequired()])
