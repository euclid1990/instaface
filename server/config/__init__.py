from . import app
from . import database
from . import jwt
from . import mail

class Config(object):
    APP = app
    DATABASE = database
    JWT = jwt
    MAIL = mail
