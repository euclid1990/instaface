from flask import jsonify
from flask_wtf import FlaskForm
from functools import wraps
from werkzeug.exceptions import HTTPException, default_exceptions, _aborter

def make_response(f):
    @wraps(f)
    def wrapper(*a, status=200):
        result = f(*a)
        if (isinstance(result, FlaskForm)):
            status = 400
            return jsonify({'success': False, 'messages': [], 'errors': result.errors}), status
        else:
            return jsonify({'success': True, 'messages': [result], 'errors': []})
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
        return jsonify({'success': False, 'messages': [h.description]}), h.code
    return handle
