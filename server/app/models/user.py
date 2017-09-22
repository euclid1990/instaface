from app import sa, bcrypt
from datetime import datetime
from marshmallow import fields
from .base import (Base, Mixin)

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

    fillable = ['name', 'username', 'email', 'password', 'phone', 'gender', 'status', 'about']
    output = ('id', 'username', 'email', 'phone', 'gender', 'status', 'about', 'roles', 'created_at', 'updated_at', 'deleted_at')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, input_password):
        return bcrypt.check_password_hash(self.password, input_password)

    @classmethod
    def attempt_login(cls, email, password):
        print(email)
        user = User.query.filter_by(email=email).first()
        print(user)
        if user is not None:
            return user
        else:
            return None
