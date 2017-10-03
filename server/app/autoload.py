import os
import sys
from pathlib import Path
from dotenv import load_dotenv

class Autoload:
    def __init__(self, app):
        self.app = app

    def run(self):
        self.dotenv()
        self.config()
        self.config_wtform()
        self.config_sqlalchemy()
        self.config_jwt()
        self.config_mail()
        self.config_redis()

    def dotenv(self):
        dotenv_path = os.path.join(Path(__file__).resolve().parents[1], '.env')
        load_dotenv(dotenv_path)

    def config(self):
        self.app.config.from_object('config.Config')
        # The JWT secret key needed for symmetric based signing algorithms, such as HS*
        self.app.config['SECRET_KEY'] = self.app.config['APP'].APP_KEY
        # Config server name for sendmail using celery/rq queue task
        host = self.app.config['APP'].APP_HOST
        port = self.app.config['APP'].APP_PORT
        self.app.config['SERVER_NAME'] = "{host}:{port}".format(host=host, port="" if port in (80, 443) else port)

    def config_wtform(self):
        # Disable csrf protection
        self.app.config['WTF_CSRF_ENABLED'] = False

    def mysql_uri(self):
        dbEnv = self.app.config['DATABASE']
        return "mysql+{}://{}:{}@localhost:{}/{}".format(
            dbEnv.MYSQL_DRIVER,
            dbEnv.MYSQL_USERNAME,
            dbEnv.MYSQL_PASSWORD,
            dbEnv.MYSQL_PORT,
            dbEnv.MYSQL_DATABASE)

    def config_sqlalchemy(self):
        # Display SQL queries for debug
        self.app.config['SQLALCHEMY_ECHO'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # Config database uri
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.mysql_uri()

    def config_jwt(self):
        jwtEnv = self.app.config['JWT']
        self.app.config['JWT_BLACKLIST_ENABLED'] = jwtEnv.JWT_BLACKLIST_ENABLED
        self.app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = jwtEnv.JWT_BLACKLIST_TOKEN_CHECKS

    def config_mail(self):
        mailEnv = self.app.config['MAIL']
        self.app.config['MAIL_SERVER'] = mailEnv.MAIL_SERVER
        self.app.config['MAIL_PORT'] = mailEnv.MAIL_PORT
        self.app.config['MAIL_USE_TLS'] = mailEnv.MAIL_USE_TLS
        self.app.config['MAIL_USERNAME'] = mailEnv.MAIL_USERNAME
        self.app.config['MAIL_PASSWORD'] = mailEnv.MAIL_PASSWORD
        self.app.config['MAIL_DEFAULT_SENDER'] = mailEnv.MAIL_DEFAULT_SENDER

    def config_redis(self):
        redisEnv = self.app.config['REDIS']
        self.app.config['REDIS_HOST'] = redisEnv.REDIS_HOST
        self.app.config['REDIS_PORT'] = redisEnv.REDIS_PORT
        self.app.config['REDIS_PASSWORD'] = redisEnv.REDIS_PASSWORD

