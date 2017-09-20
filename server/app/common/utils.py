from flask import jsonify
from flask_wtf import FlaskForm
from functools import wraps
from werkzeug.exceptions import HTTPException, default_exceptions, _aborter
from sqlalchemy.exc import DatabaseError, IntegrityError, OperationalError, StatementError


def make_response(f):
    @wraps(f)
    def wrapper(*a, status=200):
        result = f(*a)
        # Incoming request parameters do not pass the given validation rules
        if (isinstance(result, FlaskForm)):
            status = 400
            return jsonify({'success': False, 'errors': result.errors}), status
        success, message, data = result.get('success', True), result.get('message', ""), result.get('data', {})
        return jsonify({'success': success, 'message': message, 'data': data}), status
    return wrapper

def register_missing_exception():
    class FourZeroTwoException(HTTPException):
        code = 402
        description = "Payment Required"

    default_exceptions[402] = FourZeroTwoException
    _aborter.mapping[402] = FourZeroTwoException

def custom_handle_http_exception(app):
    """Overrides the default http exception handler to return JSON."""
    handle_http_exception = app.handle_http_exception
    @wraps(handle_http_exception)
    def handle(exception):
        h = handle_http_exception(exception)
        return jsonify({'success': False, 'messages': h.description}), h.code
    return handle

def error_handle(error):
    status = 400
    sqlalchemyErrors = (DatabaseError, IntegrityError, OperationalError, StatementError)
    if (isinstance(error, sqlalchemyErrors)):
        status = getattr(error, 'status_code', 400)
        message = getattr(error, 'message', str(error))
        if hasattr(error, 'orig'):
            body = str(error.orig).split(' ')
            message = ' '.join(body[2:])
        info = {'sql': error.statement, 'params': error.params}
    else:
        message = getattr(error, 'message', None)
    return jsonify({'success': False, 'message': message}), status
