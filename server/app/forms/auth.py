from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from .validators import Unique
from app.common import Constants
from app.models import User

class AuthForm(object):
    class Register(FlaskForm):
        name = StringField('Full name', validators=[
            DataRequired(),
            Length(min=Constants.USER_NAME_MIN_LENGTH, max=Constants.USER_NAME_MAX_LENGTH)
        ])
        email = StringField('Email', validators=[
            DataRequired(),
            Email(),
            Unique(User, User.email, message='There is already an account with that email.')
        ])
        password = PasswordField('Password', validators=[
            DataRequired(),
            Length(min=Constants.USER_PASSWORD_MIN_LENGTH, max=Constants.USER_PASSWORD_MAX_LENGTH),
            EqualTo('password_confirm', message='Password and confirmation password do not match')
        ])
        password_confirm = PasswordField('Password Confirmation')
        agreed = BooleanField('Agreed TOS', validators=[DataRequired()])

    class Login(FlaskForm):
        email = StringField('Email', validators=[DataRequired(), Email()])
        password = PasswordField('Password', validators=[DataRequired()])
