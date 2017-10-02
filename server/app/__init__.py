from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.orm import mapper
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    jwt_refresh_token_required,
    create_access_token,
    create_refresh_token,
    get_raw_jwt,
    get_jwt_identity,
)
from .autoload import Autoload
from app.common import (
    register_missing_exception,
    custom_handle_http_exception,
    error_handle,
    setup_schema,
    send_mail_util,
    jwt_expired_token_loader,
    jwt_invalid_token_loader,
    jwt_unauthorized_loader,
    jwt_revoked_token_loader,
    jwt_token_in_blacklist_loader,
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

# Setup the Bcrypt extension
bcrypt = Bcrypt(app)

# Setup the Flask-Sqlalchemy extension
sa = SQLAlchemy(app)
# Listen for the SQLAlchemy event and run setup_schema
from app.models import Base
event.listen(mapper, 'after_configured', setup_schema(Base, sa.session))

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)

@jwt.unauthorized_loader
def _(err):
    return jwt_unauthorized_loader(err)

@jwt.invalid_token_loader
def _(err):
    return jwt_invalid_token_loader(err)

@jwt.expired_token_loader
def _():
    return jwt_expired_token_loader()

@jwt.revoked_token_loader
def _():
    return jwt_revoked_token_loader()

from app.models import UserAccessToken
@jwt.token_in_blacklist_loader
def _(decoded_token):
    print(decoded_token)
    return jwt_token_in_blacklist_loader(UserAccessToken, decoded_token)

# Setup the Flask-Mail extension
mail = Mail(app)

def send_mail(to, subject, path_to_template, data):
    return send_mail_util(mail, app.config['MAIL_DEFAULT_SENDER'], to, subject, path_to_template, data)

# Register all blueprints
from app.views import home
from app.views import auth
app.register_blueprint(home.mod)
app.register_blueprint(auth.mod)
