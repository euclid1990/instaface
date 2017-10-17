from flask import Blueprint, request, jsonify, abort
from app.models import User
from app.common import (
    make_response,
    make_validate,
)

mod = Blueprint('validate', __name__, url_prefix='/validate')

@mod.route('/unique_email', methods=['POST'])
@make_response
def unique_email():
    data = request.json
    email = data['email']
    result = User.query.filter_by(email=email).first()
    if (result):
        return {'message': "This email is not available for registration.", 'data': { 'exist': True }}
    return {'message': "This email is still available for registration.", 'data': { 'exist': False }}
