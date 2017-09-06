from flask import Blueprint, render_template

mod = Blueprint('auth', __name__)

@mod.route('/auth/login')
def login():
    return 'Login'
