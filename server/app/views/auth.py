from flask import Blueprint, request, jsonify, abort
from app import sa, jwt, jwt_required
from app.models import User, UserAccessToken
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
        name, email, password = request.form['name'], request.form['email'].format(num), request.form['password']

        result = User.register(dict(name=name, email=email, password=password))
        return {'message': "You have registered successfully.", 'data': {'user': User.json(result)}}
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
        access_token = UserAccessToken.create(user_id=result.id)
        return {'message': "You have logged in successfully.", 'data': {'access_token': access_token}}
    return form

@mod.route('/logout')
@jwt_required
@make_response
def logout():
    return {'message': "You have logged out successfully.", 'data': {}}

@mod.route('/forgot')
def forgot():
    return 'Forgot'

@mod.route('/reset')
def reset():
    return 'Reset'
