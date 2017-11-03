from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class Chatwork(Base, Mixin):

    __tablename__ = 'chatworks'
    id = sa.Column(sa.Integer, primary_key=True)
    project_id = sa.Column(sa.Integer, sa.ForeignKey('projects.id'), nullable=False)
    room_id = sa.Column(sa.String(255), unique=True, nullable=False)
    room_name = sa.Column(sa.String(255), nullable=False)
    unread_num = sa.Column(sa.Integer, default=0)
    message_num = sa.Column(sa.Integer, default=0)
    mytask_num = sa.Column(sa.Integer, default=0)

    project = sa.relationship('Project', back_populates='chatwork')

    fillable = ['project_id', 'room_id', 'room_name', 'unread_num', 'message_num', 'mytask_num']
    output = ('project_id', 'room_id', 'room_name', 'unread_num', 'message_num', 'mytask_num')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
