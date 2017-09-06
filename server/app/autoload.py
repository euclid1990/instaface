import sys

class Autoload:
    def __init__(self, app):
        self.app = app

    def run(self):
        self.config()

    def config(self):
        self.app.config.from_object('config.Config')
