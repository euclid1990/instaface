import factory
import random
from app import models
from .base_factory import BaseFactory

class RoleFactory(BaseFactory):
    class Meta:
        model = models.Role

    name = factory.Faker('name')
    code = factory.Sequence(lambda n: n)
