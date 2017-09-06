import sys

class Autoload:
    def __init__(self, app):
        self.app = app

    def config(self):
        self.app.config.from_object('config.Config')
