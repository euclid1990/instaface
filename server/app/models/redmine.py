from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class Redmine(Base, Mixin):

    __tablename__ = 'redmines'
    id = sa.Column(sa.Integer, primary_key=True)
    project_id = sa.Column(sa.Integer, sa.ForeignKey('projects.id'), nullable=False)
    url = sa.Column(sa.String(255), nullable=False)
    pj_identifier = sa.Column(sa.String(255), nullable=False)
    pj_id = sa.Column(sa.Integer, nullable=False)
    access_token = sa.Column(sa.String(255), nullable=False)

    # Define unique constraints
    __table_args__ = (sa.UniqueConstraint('url', 'pj_identifier', 'pj_id', name='unique_project'),)

    project = sa.relationship('Project', back_populates='redmine')

    fillable = ['project_id', 'url', 'pj_identifier', 'pj_id', 'access_token']
    output = ('project_id', 'url', 'pj_identifier', 'pj_id', 'access_token')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
