from flask import Blueprint, request, jsonify, abort
from app import sa
from app.models import User
from app.forms import AuthForm
from app.utils import make_response

mod = Blueprint('auth', __name__, url_prefix='/auth')
Form = AuthForm()

@mod.route('/register', methods=['POST'])
@make_response
def register():
    abort(402)
    form = Form.Register()
    if form.validate_on_submit():
        result = User.updateById(50, dict(email='username_email@example.com'))
        return 'You have successfully registered.'
    return form

@mod.route('/login')
def login():
    return 'Login'

@mod.route('/logout')
def logout():
    return 'Logout'

@mod.route('/forgot')
def forgot():
    return 'Forgot'

@mod.route('/reset')
def reset():
    return 'Reset'
