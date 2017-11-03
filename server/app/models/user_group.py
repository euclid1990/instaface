from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class UserGroup(Base, Mixin):

    __tablename__ = 'user_groups'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    group_id = sa.Column(sa.Integer, sa.ForeignKey('groups.id'), nullable=False)

    # Define a bidirectional relationship in many-to-many with secondary
    user = sa.relationship('User', primaryjoin="and_(UserGroup.user_id == User.id, UserGroup.deleted_at == None)", backref=sa.backref("user_groups"))
    group = sa.relationship('Group', primaryjoin="and_(UserGroup.group_id == Group.id, UserGroup.deleted_at == None)", backref=sa.backref("user_groups"))

    fillable = ['user_id', 'group_id', 'user', 'group']
    output = ('id', 'user_id', 'group_id')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

