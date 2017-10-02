from flask import Blueprint, request, jsonify, abort
from app import (
    sa,
    jwt,
    jwt_required,
    jwt_refresh_token_required,
    get_raw_jwt,
    get_jwt_identity,
    send_mail,
)
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
        send_mail(
            email,
            'Confirm your account on Instaface',
            'auth/mails/register.html',
            {'active_token': result.active_token}
        )
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
        access_token, refresh_token = UserAccessToken.create(user_id=result.id, with_refresh_token=True)
        return {'message': "You have logged in successfully.", 'data': {'access_token': access_token, 'refresh_token': refresh_token}}
    return form

@mod.route('/logout')
@jwt_required
@make_response
def logout():
    jwt = get_raw_jwt()
    result = UserAccessToken.add_token_to_blacklist(jwt['jti'])
    return {'message': "You have logged out successfully.", 'data': {'result': result}}

@mod.route('/refresh')
@jwt_refresh_token_required
@make_response
def refresh():
    user_id = get_jwt_identity()
    access_token = UserAccessToken.create(user_id=user_id, with_refresh_token=False)
    return {'message': "You have refreshed token successfully.", 'data': {'access_token': access_token}}


@mod.route('/active/<active_token>', methods=['GET'])
@make_response
def active(active_token):
    result = User.active(active_token)
    if result:
        return {'message': "You have active account successfully.", 'data': {'result': result}}
    return {'message': "Your account has already been activated.", 'data': {'result': result}}

@mod.route('/forgot')
def forgot():
    return 'Forgot'

@mod.route('/reset')
def reset():
    return 'Reset'
