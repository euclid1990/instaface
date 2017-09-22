from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class UserGroup(Base, Mixin):

    __tablename__ = 'user_groups'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    group_id = sa.Column(sa.Integer, sa.ForeignKey('groups.id'), nullable=False)

    fillable = ['user_id', 'group_id']
    output = ('id', 'user_id', 'group_id')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def set_schema(cls):
        cls.schema = UserGroupSchema

