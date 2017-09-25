import factory
from app import app, sa
from database.seeds import (
    UserSeeder,
    RoleSeeder,
    GroupSeeder,
    UserRoleSeeder,
    UserGroupSeeder,
)

class SeedCommand(object):
    @staticmethod
    def run(drop):
        print("------ [START] Database seeding ------")
        # Init and Reset database
        if (drop):
            sa.drop_all(bind=None)
            sa.create_all(bind=None)

        roles = RoleSeeder.exec()
        groups = GroupSeeder.exec()
        users = UserSeeder.exec(user_roles=roles, user_groups=groups)

        sa.session.commit()
        print("------ [COMPLETE] Database seeding ------")
