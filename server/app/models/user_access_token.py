from app import sa, create_access_token
from datetime import datetime, timedelta
from marshmallow_sqlalchemy import ModelSchema
from .base import (Base, Mixin)

class UserAccessToken(Base, Mixin):

    __tablename__ = 'user_access_tokens'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, nullable=False)
    value = sa.Column(sa.Text(300))

    fillable = ['user_id', 'value']
    output = ('id', 'user_id', 'value')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def set_schema(cls):
        cls.schema = UserAccessTokenSchema

    @classmethod
    def create(cls, user_id):
        expires = timedelta(days=7)
        access_token = create_access_token(identity=user_id, expires_delta=expires)
        super().create(dict(user_id=user_id, value=access_token))
        return access_token
