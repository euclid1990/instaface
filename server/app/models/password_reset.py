from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class PasswordReset(Base, Mixin):

    __tablename__ = 'password_resets'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    token = sa.Column(sa.String(255), nullable=False, index=True)

    users = sa.relationship('User', back_populates='password_resets')

    fillable = ['user_id', 'token']
    output = ('id', 'user_id', 'token')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
