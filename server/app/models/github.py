from app import sa
from datetime import datetime
from .base import (Base, Mixin)

class Github(Base, Mixin):

    __tablename__ = 'githubs'
    id = sa.Column(sa.Integer, primary_key=True)
    project_id = sa.Column(sa.Integer, sa.ForeignKey('projects.id'), nullable=False)
    repo_id = sa.Column(sa.String(255), nullable=False)
    repo_name = sa.Column(sa.String(255), nullable=False)
    repo_full_name = sa.Column(sa.String(255), nullable=False)
    repo_private = sa.Column(sa.Boolean, default=False)
    repo_fork = sa.Column(sa.Boolean, default=False)
    repo_has_issues = sa.Column(sa.Boolean, default=False)
    repo_has_wiki = sa.Column(sa.Boolean, default=True)
    repo_has_pages = sa.Column(sa.Boolean, default=False)
    repo_has_downloads = sa.Column(sa.Boolean, default=True)
    repo_archived = sa.Column(sa.Boolean, default=False)
    repo_url = sa.Column(sa.String(255), nullable=False)
    repo_hooks_url = sa.Column(sa.String(255), nullable=False)
    repo_pulls_url = sa.Column(sa.String(255), nullable=False)
    repo_comments_url = sa.Column(sa.String(255), nullable=False)
    repo_commits_url = sa.Column(sa.String(255), nullable=False)
    repo_ssh_url = sa.Column(sa.String(255), nullable=False)
    repo_default_branch = sa.Column(sa.String(255), nullable=False, default="master")
    repo_pushed_at = sa.Column(sa.DateTime())

    # Define unique constraints
    __table_args__ = (sa.UniqueConstraint('repo_url', 'repo_id', 'repo_full_name', name='unique_repository'),)

    project = sa.relationship('Project', back_populates='github')

    fillable = ['project_id', 'repo_id', 'repo_name', 'repo_full_name', 'repo_private', 'repo_fork', 'repo_has_issues', 'repo_has_wiki', 'repo_has_pages', \
                'repo_has_downloads', 'repo_archived', 'repo_url', 'repo_hooks_url', 'repo_pulls_url', 'repo_comments_url', 'repo_commits_url', 'repo_ssh_url', 'repo_default_branch', 'repo_pushed_at']
    output = ('project_id', 'repo_id', 'repo_name', 'repo_full_name', 'repo_private', 'repo_fork', 'repo_has_issues', 'repo_has_wiki', 'repo_has_pages', \
                'repo_has_downloads', 'repo_archived', 'repo_url', 'repo_hooks_url', 'repo_pulls_url', 'repo_comments_url', 'repo_commits_url', 'repo_ssh_url', 'repo_default_branch', 'repo_pushed_at')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
