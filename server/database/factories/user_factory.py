import factory
import random
from app import models
from .base_factory import BaseFactory

class UserFactory(BaseFactory):
    class Meta:
        model = models.User

    @factory.sequence
    def phone(n):
        a = n // 10000
        b = n % 10000
        return "%03d-555-%04d" % (a, b)

    name = factory.Faker('name')
    username = factory.Faker('user_name')
    email = factory.LazyAttributeSequence(lambda o, n: "{username}{id}@example.com".format(username=o.username, id=n))
    password = factory.PostGenerationMethodCall('set_password', 'defaultPassword')
    gender = factory.Faker('random_element', elements=list(models.User.GENDER.values()))
    status = factory.Faker('random_element', elements=list(models.User.STATUS.values()))
    about = factory.Faker('text', max_nb_chars=300)

    @factory.post_generation
    def user_roles(self, create, roles, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if roles:
            # A list of roles were passed in, use them
            role = random.choice(roles)
            self.user_roles.append(models.UserRole(user=self, role=role))

    @factory.post_generation
    def user_groups(self, create, groups, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if groups:
            # A list of groups were passed in, use them
            group = random.choice(groups)
            # print(group.id)
            self.user_groups.append(models.UserGroup(user=self, group=group))
