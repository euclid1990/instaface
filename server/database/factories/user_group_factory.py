import factory
import random
from app import models
from .base_factory import BaseFactory
from .user_factory import UserFactory
from .group_factory import GroupFactory

class UserGroupFactory(BaseFactory):
    class Meta:
        model = models.UserGroup

    user = factory.SubFactory(UserFactory)
    group = factory.SubFactory(GroupFactory)
