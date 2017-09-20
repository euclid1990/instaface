from flask import Blueprint, request, jsonify, abort
from app import sa
from app.models import User
from app.forms import AuthForm
from app.common import make_response

mod = Blueprint('auth', __name__, url_prefix='/auth')
Form = AuthForm()

@mod.route('/register', methods=['POST'])
@make_response
def register():
    form = Form.Register()
    if form.validate_on_submit():
        import random
        num = random.choice(list(x for x in range(100)))
        result = User.create(dict(name=request.form['name'], email=request.form['email'].format(num), password=request.form['password']))
        return {'message': "", 'data': {'user': User.json(result)}}
    return form

@mod.route('/login', methods=['POST'])
@make_response
def login():
    form = Form.Login()
    if form.validate_on_submit():
        email, password = request.form['email'], request.form['password']
        result = User.attempt_login(email, password)
        if result is None:
            return {'success': False, 'message': "These credentials do not match our records.", 'data': {}}
        return {'message': "", 'data': {'user': User.json(result)}}
    return form

@mod.route('/logout')
def logout():
    return 'Logout'

@mod.route('/forgot')
def forgot():
    return 'Forgot'

@mod.route('/reset')
def reset():
    return 'Reset'
