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
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.mysql_uri()

    def dotenv(self):
        dotenv_path = os.path.join(Path(__file__).resolve().parents[1], '.env')
        load_dotenv(dotenv_path)

    def config(self):
        self.app.config.from_object('config.Config')

    def mysql_uri(self):
        dbEnv = self.app.config['DATABASE']
        return "mysql+{}://{}:{}@localhost:{}/{}".format(
            dbEnv.MYSQL_DRIVER,
            dbEnv.MYSQL_USERNAME,
            dbEnv.MYSQL_PASSWORD,
            dbEnv.MYSQL_PORT,
            dbEnv.MYSQL_DATABASE)
