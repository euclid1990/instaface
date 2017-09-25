from database.factories import RoleFactory
from app.common import Constants

class RoleSeeder:
    @staticmethod
    def exec():
        admin = RoleFactory.create(name=Constants.ROLE_ADMIN_NAME, code=Constants.ROLE_ADMIN_CODE)
        member = RoleFactory.create(name=Constants.ROLE_MEMBER_NAME, code=Constants.ROLE_MEMBER_CODE)
        return (admin, member)
