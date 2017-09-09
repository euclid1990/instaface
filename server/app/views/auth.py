from flask import Blueprint, render_template

mod = Blueprint('auth', __name__, url_prefix='/auth')

@mod.route('/register')
def register():
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
