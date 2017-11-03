from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class ProjectMember(Base, Mixin):

    __tablename__ = 'project_members'
    id = sa.Column(sa.Integer, primary_key=True)
    project_id = sa.Column(sa.Integer, sa.ForeignKey('projects.id'), nullable=False)
    member_id = sa.Column(sa.Integer, sa.ForeignKey('members.id'), nullable=False)

    # Define a bidirectional relationship in many-to-many with secondary
    project = sa.relationship('Project', backref=sa.backref("project_members"))
    member = sa.relationship('Member', backref=sa.backref("project_members"))

    fillable = ['project_id', 'member_id', 'member', 'project']
    output = ('id', 'project_id', 'member_id')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
