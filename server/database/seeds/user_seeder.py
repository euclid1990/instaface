from database.factories import UserFactory

class UserSeeder:
    @staticmethod
    def exec():
        UserFactory.create_batch(10)
