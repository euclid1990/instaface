from database.factories import GroupFactory
from app.common import Constants

class GroupSeeder:
    @staticmethod
    def exec():
        GroupFactory.create(name=Constants.GROUP_ADMIN_NAME, code=Constants.GROUP_ADMIN_CODE)
        GroupFactory.create(name=Constants.GROUP_OPERATOR_NAME, code=Constants.GROUP_OPERATOR_CODE)
