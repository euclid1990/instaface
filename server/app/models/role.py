from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class Role(Base, Mixin):

    __tablename__ = 'roles'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    code = sa.Column(sa.SmallInteger(), unique=True)

    # Many to Many adds an "user_roles" table between two classes.
    # users = sa.relationship("UserRole", back_populates="role")
    users = sa.relationship('User', secondary='user_roles', viewonly=True)

    fillable = ['name', 'code']
    output = ('id', 'name', 'code')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def set_schema(cls):
        cls.schema = RoleSchema

