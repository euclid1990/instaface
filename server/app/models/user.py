from app import sa
from datetime import datetime
from .base import Base

class User(Base):
    GENDER = {'UNKNOWN': 0, 'MALE': 1, 'FEMALE': 2}
    STATUS = {'INACTIVE': 0, 'ACTIVE': 1, 'BANNED': 2}

    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    username = sa.Column(sa.String(30), unique=True)
    email = sa.Column(sa.String(255), unique=True)
    password = sa.Column(sa.String(60), nullable=False)
    birthday = sa.Column(sa.Date());
    phone = sa.Column(sa.String(15))
    gender = sa.Column(sa.SmallInteger(), default=GENDER['UNKNOWN'])
    status = sa.Column(sa.SmallInteger(), default=STATUS['INACTIVE'])
    about = sa.Column(sa.Text(500))
    active_token = sa.Column(sa.String(255))
    jwt_token = sa.Column(sa.Text(300))
    password_changed_at = sa.Column(sa.DateTime())
    logged_in_at = sa.Column(sa.DateTime())
    logged_out_at = sa.Column(sa.DateTime())

    def __init__(self, arg):
        super().__init__()
        self.arg = arg
