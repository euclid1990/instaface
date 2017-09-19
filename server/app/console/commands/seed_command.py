import factory
from app import app, sa
from database.seeds import UserSeeder

class SeedCommand(object):
    @staticmethod
    def run(drop):
        # Init and Reset database
        if (drop):
            sa.drop_all(bind=None)
            sa.create_all(bind=None)

        UserSeeder.exec()
        sa.session.commit()
