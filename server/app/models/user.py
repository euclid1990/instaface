from datetime import datetime
from marshmallow import fields
from app import sa, bcrypt
from app.common import Constants
from .base import (Base, Mixin)
from .role import Role
from .user_role import UserRole
from .group import Group
from .user_group import UserGroup

class User(Base, Mixin):
    GENDER = {'UNKNOWN': 0, 'MALE': 1, 'FEMALE': 2}
    STATUS = {'INACTIVE': 0, 'ACTIVE': 1, 'BANNED': 2}

    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    username = sa.Column(sa.String(30), unique=True)
    email = sa.Column(sa.String(255), unique=True, nullable=False)
    password = sa.Column(sa.String(60), nullable=False)
    birthday = sa.Column(sa.Date());
    phone = sa.Column(sa.String(15))
    gender = sa.Column(sa.SmallInteger(), default=GENDER['UNKNOWN'])
    status = sa.Column(sa.SmallInteger(), default=STATUS['INACTIVE'])
    about = sa.Column(sa.Text(500))
    active_token = sa.Column(sa.String(255))
    password_changed_at = sa.Column(sa.DateTime())
    logged_in_at = sa.Column(sa.DateTime())
    logged_out_at = sa.Column(sa.DateTime())

    # Many to Many adds an "user_roles" table between two classes.
    # roles = sa.relationship("UserRole", back_populates="user")
    roles = sa.relationship('Role', secondary='user_roles', viewonly=True)

    groups = sa.relationship('Group', secondary='user_groups', viewonly=True)

    fillable = ['name', 'username', 'email', 'password', 'birthday', 'phone', 'gender', 'status', 'about']
    output = ('id', 'username', 'email', 'phone', 'gender', 'status', 'about', 'roles', 'groups', 'created_at', 'updated_at', 'deleted_at')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, input_password):
        return bcrypt.check_password_hash(self.password, input_password)

    @classmethod
    def register(cls, data):
        data = dict((key, value) for (key, value) in data.items() if (key in cls.fillable))
        user = cls(**data)
        # Assign role to user
        role = Role.query.filter_by(code=Constants.ROLE_MEMBER_CODE, deleted_at=None).first()
        user.user_roles.append(UserRole(user=user, role=role))
        # Commit user to DB
        sa.session.add(user)
        sa.session.commit()
        return user

    @classmethod
    def attempt_login(cls, email, password):
        user = User.query.filter_by(email=email).first()
        print(user)
        if user is not None:
            return user
        else:
            return None

    @classmethod
    def change_group(cls, id, group_code):
        user = User.query.filter_by(id=id, deleted_at=None).first()
        group = Group.query.filter_by(code=group_code, deleted_at=None).first()
        if user and group:
            # Assign group to user
            has_group = user.groups
            # import pdb; pdb.set_trace();
            if not has_group:
                user.user_groups.append(UserGroup(user=user, group=group))
            else:
                user.user_groups[0].query.filter_by(id=user.id).update(dict(group_id=group.id))
            sa.session.commit()
            return True
        return False
