from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class UserProject(Base, Mixin):

    __tablename__ = 'user_projects'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    project_id = sa.Column(sa.Integer, sa.ForeignKey('projects.id'), nullable=False)

    # Define a bidirectional relationship in many-to-many with secondary
    user = sa.relationship('User', backref=sa.backref("user_projects"))
    project = sa.relationship('Project', backref=sa.backref("user_projects"))

    fillable = ['user_id', 'project_id', 'user', 'project']
    output = ('id', 'user_id', 'project_id')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
