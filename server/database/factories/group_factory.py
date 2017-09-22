import factory
import random
from app import models
from .base_factory import BaseFactory

class GroupFactory(BaseFactory):
    class Meta:
        model = models.Group

    name = factory.Faker('name')
    code = factory.Sequence(lambda n: n)
