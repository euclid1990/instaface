from . import (
    app,
    database,
    jwt,
    mail,
    redis,
    github,
    chatwork,
)

class Config(object):
    APP = app
    DATABASE = database
    JWT = jwt
    MAIL = mail
    REDIS = redis
    GITHUB = github
    CHATWORK = chatwork
