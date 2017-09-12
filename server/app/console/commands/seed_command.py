import factory
from app import app, sa
from database.seeds import UserSeeder

class SeedCommand(object):
    @staticmethod
    def run():
        UserSeeder.exec()
        sa.session.commit()
