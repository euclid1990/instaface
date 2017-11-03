from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class Group(Base, Mixin):

    __tablename__ = 'groups'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    code = sa.Column(sa.SmallInteger(), unique=True)

    users = sa.relationship('User', secondary='user_groups', viewonly=True)
    projects = sa.relationship('Project', back_populates='group')

    fillable = ['name', 'code']
    output = ('id', 'name')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

