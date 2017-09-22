from database.factories import UserRoleFactory

class UserRoleSeeder:
    @staticmethod
    def exec():
        UserRoleFactory.create_batch(10)
