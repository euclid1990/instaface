from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from .autoload import Autoload

app = Flask(__name__)

auto = Autoload(app)
auto.run()

bcrypt = Bcrypt(app)

sa = SQLAlchemy(app)

from app.views import home
from app.views import auth
app.register_blueprint(home.mod)
app.register_blueprint(auth.mod)
