from . import app
from . import database
from . import jwt
from . import mail
from . import redis

class Config(object):
    APP = app
    DATABASE = database
    JWT = jwt
    MAIL = mail
    REDIS = redis
