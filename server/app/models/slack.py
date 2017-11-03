from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class Slack(Base, Mixin):

    __tablename__ = 'slacks'
    id = sa.Column(sa.Integer, primary_key=True)
    project_id = sa.Column(sa.Integer, sa.ForeignKey('projects.id'), nullable=False)
    url = sa.Column(sa.String(255), nullable=False)
    channel_id = sa.Column(sa.String(255), nullable=False)
    is_private = sa.Column(sa.Boolean, default=False)
    unread_count = sa.Column(sa.Integer, default=0)
    unread_count_display = sa.Column(sa.Integer, default=0)

    project = sa.relationship('Project', back_populates='slack')

    fillable = ['project_id', 'url', 'channel_id', 'is_private', 'unread_count', 'unread_count_display']
    output = ('project_id', 'url', 'channel_id', 'is_private', 'unread_count', 'unread_count_display')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
