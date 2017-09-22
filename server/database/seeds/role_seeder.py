from database.factories import RoleFactory
from app.common import Constants

class RoleSeeder:
    @staticmethod
    def exec():
        RoleFactory.create(name=Constants.ROLE_ADMIN_NAME, code=Constants.ROLE_ADMIN_CODE)
        RoleFactory.create(name=Constants.ROLE_MEMBER_NAME, code=Constants.ROLE_MEMBER_CODE)

