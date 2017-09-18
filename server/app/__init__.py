from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from .autoload import Autoload
from .utils import custom_handle_http_exception

app = Flask(__name__)
app.handle_http_exception = custom_handle_http_exception(app)

auto = Autoload(app)
auto.run()

bcrypt = Bcrypt(app)

sa = SQLAlchemy(app)

from app.views import home
from app.views import auth
app.register_blueprint(home.mod)
app.register_blueprint(auth.mod)
