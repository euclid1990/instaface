import factory
import random
from app import models
from .base_factory import BaseFactory
from .user_factory import UserFactory
from .role_factory import RoleFactory

class UserRoleFactory(BaseFactory):
    class Meta:
        model = models.UserRole

    user = factory.SubFactory(UserFactory)
    role = factory.SubFactory(RoleFactory)
