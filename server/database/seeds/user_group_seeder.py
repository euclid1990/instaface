from database.factories import UserGroupFactory

class UserGroupSeeder:
    @staticmethod
    def exec():
        UserGroupFactory.create_batch(10)
