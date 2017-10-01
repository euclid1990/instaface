from . import app
from . import database
from . import jwt

class Config(object):
    APP = app
    DATABASE = database
    JWT = jwt
