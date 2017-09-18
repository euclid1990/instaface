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
    form = Form.Register()
    if form.validate_on_submit():
        result = User.create(dict(name="123", email='66sssdddssdsdssss66@example.com', password="123456"))
        return {'message': "", 'data': {'user': User.json(result)}}
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
