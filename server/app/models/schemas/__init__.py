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
    Project,
    UserProject,
    Member,
    ProjectMember,
    Github,
    Redmine,
    Chatwork,
    Slack,
)

class UserSchema(ModelSchema):
    # Avoid infinite recursion
    roles = fields.Nested('RoleSchema', many=True, only=('id', 'name', 'code'), exclude=('users', 'user_roles'))
    groups = fields.Nested('GroupSchema', many=True, only=('id', 'name', 'code'), exclude=('users', 'user_groups'))
    password_resets = fields.Nested('PasswordResetSchema', many=True, only=('id', 'user_id', 'token'), exclude=('users'))
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


class ProjectSchema(ModelSchema):
    # Avoid infinite recursion
    users = fields.Nested('UserSchema', many=True, only=('id', 'name'), exclude=('projects'))
    members = fields.Nested('MemberSchema', many=True, only=('id', 'name', 'gmail'), exclude=('projects'))
    group = fields.Nested('RoleSchema', many=True, only=('id', 'name', 'code'), exclude=('users', 'user_groups', 'projects'))
    github = fields.Nested('GithubSchema', many=True, only=('id'), exclude=('project'))
    redmine = fields.Nested('RedmineSchema', many=True, only=('id'), exclude=('project'))
    chatwork = fields.Nested('ChatworkSchema', many=True, only=('id'), exclude=('project'))
    slack = fields.Nested('SlackSchema', many=True, only=('id'), exclude=('project'))

    class Meta:
        model = Project


class UserProjectSchema(ModelSchema):
    class Meta:
        model = UserProject


class MemberSchema(ModelSchema):
    class Meta:
        model = Member


class ProjectMemberSchema(ModelSchema):
    class Meta:
        model = ProjectMember


class GithubSchema(ModelSchema):
    class Meta:
        model = Github


class RedmineSchema(ModelSchema):
    class Meta:
        model = Redmine


class ChatworkSchema(ModelSchema):
    class Meta:
        model = Chatwork


class SlackSchema(ModelSchema):
    class Meta:
        model = Slack
