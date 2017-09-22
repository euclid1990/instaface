from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.orm import mapper
from flask_jwt_extended import JWTManager, jwt_required
from .autoload import Autoload
from app.common import (
    register_missing_exception,
    custom_handle_http_exception,
    error_handle,
    setup_schema,
)

app = Flask(__name__)

# Run autoload configuration
auto = Autoload(app)
auto.run()

# Handle missing 402 in default exception
register_missing_exception()
# Overrides the default http exception handler
app.handle_http_exception = custom_handle_http_exception(app)
# Set up an error handler on the app
if app.config['APP'].APP_ENV == "production":
    @app.errorhandler(Exception)
    def _(error):
        return error_handle(error)

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)

# Setup the Bcrypt extension
bcrypt = Bcrypt(app)

# Setup the Flask-Sqlalchemy extension
sa = SQLAlchemy(app)
# Listen for the SQLAlchemy event and run setup_schema
from app.models import Base
event.listen(mapper, 'after_configured', setup_schema(Base, sa.session))

# Register all blueprints
from app.views import home
from app.views import auth
app.register_blueprint(home.mod)
app.register_blueprint(auth.mod)
