from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from .autoload import Autoload
from .utils import register_missing_exception, custom_handle_http_exception

app = Flask(__name__)

# Handle missing 402 in default exception
register_missing_exception()
# Overrides the default http exception handler
app.handle_http_exception = custom_handle_http_exception(app)

# Run autoload configuration
auto = Autoload(app)
auto.run()

bcrypt = Bcrypt(app)

sa = SQLAlchemy(app)

from app.views import home
from app.views import auth
app.register_blueprint(home.mod)
app.register_blueprint(auth.mod)
