from datetime import datetime
from app import sa
from app.common import Constants
from .base import (Base, Mixin)

class Project(Base, Mixin):
    STATUS = {'NEW': 0, 'IN_PROGRESS': 1, 'CLOSED': 2}

    __tablename__ = 'projects'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    group_id = sa.Column(sa.Integer, sa.ForeignKey('groups.id'), nullable=False)
    status = sa.Column(sa.SmallInteger(), default=STATUS['NEW'])
    description = sa.Column(sa.String(255))
    start_date = sa.Column(sa.DateTime())
    end_date = sa.Column(sa.DateTime())

    users = sa.relationship('User', secondary='user_projects', viewonly=True)
    members = sa.relationship('Member', secondary='project_members', viewonly=True)
    group = sa.relationship('Group', primaryjoin="and_(Project.group_id == Group.id, Project.deleted_at == None)", uselist=False)
    github = sa.relationship('Github', uselist=False, back_populates='project')
    redmine = sa.relationship('Redmine', uselist=False, back_populates='project')
    chatwork = sa.relationship('Chatwork', uselist=False, back_populates='project')
    slack = sa.relationship('Slack', uselist=False, back_populates='project')

    fillable = ['name', 'group_id', 'status', 'description', 'start_date', 'end_date']
    output = ('name', 'group_id', 'status', 'description', 'start_date', 'end_date')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
