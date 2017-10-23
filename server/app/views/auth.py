from flask import Blueprint, request, jsonify, abort
from uuid import uuid4
from hashlib import sha256
from datetime import datetime, timedelta
from app import (
    sa,
    jwt,
    jwt_required,
    jwt_refresh_token_required,
    get_raw_jwt,
    get_jwt_identity,
    send_mail,
)
from app.models import User, UserAccessToken, PasswordReset
from app.forms import AuthForm
from app.common import (
    make_response,
    make_validate,
)

mod = Blueprint('auth', __name__, url_prefix='/auth')
Form = AuthForm()

@mod.route('/register', methods=['POST'])
@make_response
@make_validate(form_class=Form.Register)
def register():
    data = request.json
    import random
    num = random.choice(list(x for x in range(100)))
    name, email, password, gender = data['name'], data['email'].format(num), data['password'], User.GENDER.get(data['gender'], User.GENDER['UNKNOWN'])
    result = User.register(dict(name=name, email=email, password=password, gender=gender))
    send_mail(
        email,
        'Confirm your account on Instaface',
        'auth/mails/register.html',
        {'active_token': result.active_token}
    )
    return {'message': "You have registered successfully.", 'data': {'user': User.json(result)}}


@mod.route('/login', methods=['POST'])
@make_response
@make_validate(form_class=Form.Login)
def login():
    data = request.json
    email, password = data['email'], data['password']
    result = User.attempt_login(email, password)
    if result is None:
        return {'success': False, 'message': "These credentials do not match our records.", 'data': {}}
    access_token, refresh_token = UserAccessToken.create(user_id=result.id, with_refresh_token=True)
    return {'message': "You have logged in successfully.",
        'data': {'user': {'id': result.id, 'name': result.name}, 'access_token': access_token, 'refresh_token': refresh_token}}


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


@mod.route('/forgot', methods=['POST'])
@make_response
@make_validate(form_class=Form.Forgot)
def forgot():
    email = request.json['email']
    user = User.query.filter_by(email=email).first()
    if user is None:
        return {'message': "The email cannot be recognized.", 'data': {}, 'success': False}
    reset_token = sha256(str(uuid4()).encode('utf-8')).hexdigest()
    password_reset = PasswordReset.create(dict(user_id=user.id, token=reset_token))
    send_mail(
        email,
        'Instaface password reset link',
        'auth/mails/forgot.html',
        {'name': user.name, 'reset_token': reset_token}
    )
    return {'message': "You have forgot password successfully.", 'data': {}}


@mod.route('/reset/<reset_token>', methods=['POST'])
@make_response
@make_validate(form_class=Form.Reset)
def reset(reset_token):
    record = PasswordReset.query.filter_by(token=reset_token, deleted_at=None).first()
    if record is None:
        return {'message': "The reset password token cannot be recognized.", 'data': {}, 'success': False}
    expired_at = record.created_at + timedelta(hours=24)
    if datetime.utcnow() > expired_at:
        return {'message': "The reset password token has expired.", 'data': {}, 'success': False}
    password = request.json['password']
    record.deleted_at = datetime.utcnow()
    User.updateById(record.user_id, dict(password=User.hash_password(password), password_changed_at=datetime.utcnow()))
    return {'message': "You have reset password successfully.", 'data': {}}


@mod.route('/password', methods=['POST'])
@jwt_required
@make_response
def password():
    user_id = get_jwt_identity()
    form = Form.Password(user_id)
    if form.validate_on_submit():
        password = request.json['new_password']
        User.updateById(user_id, dict(password=User.hash_password(password), password_changed_at=datetime.utcnow()))
        return {'message': "You have changed password successfully.", 'data': {}}
    return form
