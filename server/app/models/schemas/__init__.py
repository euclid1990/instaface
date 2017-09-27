from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from app.models import (
    User,
    UserRole,
    UserAccessToken,
    PasswordReset,
    Role,
    Group,
    UserGroup,
)

class UserSchema(ModelSchema):
    # Avoid infinite recursion
    roles = fields.Nested('RoleSchema', many=True, only=('id', 'name', 'code'), exclude=('users', 'user_roles'))
    groups = fields.Nested('GroupSchema', many=True, only=('id', 'name', 'code'), exclude=('users', 'user_groups'))
    class Meta:
        model = User


class RoleSchema(ModelSchema):
    # Avoid infinite recursion
    users = fields.Nested('UserSchema', many=True, only=('id', 'name', 'email'), exclude=('roles', 'user_roles'))
    class Meta:
        model = Role


class UserAccessTokenSchema(ModelSchema):
    class Meta:
        model = UserAccessToken


class PasswordResetSchema(ModelSchema):
    class Meta:
        model = PasswordReset


class UserRoleSchema(ModelSchema):
    class Meta:
        model = UserRole


class GroupSchema(ModelSchema):
    class Meta:
        model = Group


class UserGroupSchema(ModelSchema):
    # Avoid infinite recursion
    users = fields.Nested('UserSchema', many=True, only=('id', 'name', 'email'), exclude=('groups', 'user_groups'))
    class Meta:
        model = UserGroup
