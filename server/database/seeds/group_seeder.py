from database.factories import GroupFactory
from app.common import Constants

class GroupSeeder:
    @staticmethod
    def exec():
        admin = GroupFactory.create(name=Constants.GROUP_ADMIN_NAME, code=Constants.GROUP_ADMIN_CODE)
        operator = GroupFactory.create(name=Constants.GROUP_OPERATOR_NAME, code=Constants.GROUP_OPERATOR_CODE)
        return (admin, operator)
