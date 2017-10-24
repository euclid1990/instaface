from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from .validators import Unique, CurrentPassword
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

    class Forgot(FlaskForm):
        email = StringField('Email', validators=[DataRequired(), Email()])

    class Reset(FlaskForm):
        password = PasswordField('Password', validators=[
            DataRequired(),
            Length(min=Constants.USER_PASSWORD_MIN_LENGTH, max=Constants.USER_PASSWORD_MAX_LENGTH),
            EqualTo('password_confirm', message='Password and confirmation password do not match')
        ])
        password_confirm = PasswordField('Password Confirmation')

    class Password(FlaskForm):
        def __init__(self, user_id, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.user_id = user_id

        current_password = PasswordField('Current Password', validators=[
            DataRequired(),
            CurrentPassword(User)
        ])

        new_password = PasswordField('New Password', validators=[
            DataRequired(),
            Length(min=Constants.USER_PASSWORD_MIN_LENGTH, max=Constants.USER_PASSWORD_MAX_LENGTH),
            EqualTo('new_password_confirm', message='New password and confirmation password do not match')
        ])
        new_password_confirm = PasswordField('New Password Confirmation')
