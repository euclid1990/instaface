from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class UserRole(Base, Mixin):

    __tablename__ = 'user_roles'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    role_id = sa.Column(sa.Integer, sa.ForeignKey('roles.id'), nullable=False)

    # Define a bidirectional relationship in many-to-many with back_populates
    # user = sa.relationship("User", back_populates="roles")
    # role = sa.relationship("Role", back_populates="users")

    # Define a bidirectional relationship in many-to-many with secondary
    user = sa.relationship('User', backref=sa.backref("user_roles"))
    role = sa.relationship('Role', backref=sa.backref("user_roles"))

    fillable = ['user_id', 'role_id', 'user', 'role']
    output = ('id', 'user_id', 'role_id')

    def __init__(self, **kwargs):
        print(kwargs)
        super().__init__(**kwargs)

    @classmethod
    def set_schema(cls):
        cls.schema = UserRoleSchema

