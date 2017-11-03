from datetime import datetime
from app import sa
from app.common import Constants
from .base import (Base, Mixin)

class Member(Base, Mixin):

    __tablename__ = 'members'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    chatwork_id = sa.Column(sa.String(255))
    redmine_id = sa.Column(sa.String(255))
    github_id = sa.Column(sa.String(255))
    github_username = sa.Column(sa.String(255))
    slack_username = sa.Column(sa.String(255))
    gmail = sa.Column(sa.String(255))
    fmail = sa.Column(sa.String(255))

    fillable = ['name', 'chatwork_id', 'redmine_id', 'github_id', 'github_username', 'slack_username', 'gmail', 'fmail']
    output = ('name', 'chatwork_id', 'redmine_id', 'github_id', 'github_username', 'slack_username', 'gmail', 'fmail')

    projects = sa.relationship('Project', secondary='project_members', viewonly=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
