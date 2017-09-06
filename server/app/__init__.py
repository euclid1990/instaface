from flask import Flask
from .autoload import Autoload

app = Flask(__name__)

from app.views import home
from app.views import auth
app.register_blueprint(home.mod)
app.register_blueprint(auth.mod)

