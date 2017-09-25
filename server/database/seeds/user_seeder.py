from database.factories import UserFactory

class UserSeeder:
    @staticmethod
    def exec(user_roles, user_groups):
        users = UserFactory.create_batch(5, user_roles=user_roles, user_groups=user_groups)
        return users
