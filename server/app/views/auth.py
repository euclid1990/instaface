from flask import Blueprint, render_template
from app import sa
from app.models import User

mod = Blueprint('auth', __name__, url_prefix='/auth')

@mod.route('/register')
def register():
    try:
        User.updateById(1, dict(email='username_email@example.com'))
        sa.session.commit()
    except Exception as e:
        msg = getattr(e, 'message', repr(e))
        return msg
    return 'Register'

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
