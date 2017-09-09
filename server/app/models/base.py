from app import sa
from datetime import datetime

class Base(sa.Model):
    created_at = sa.Column(sa.DateTime)
    updated_at = sa.Column(sa.DateTime)
    deleted_at = sa.Column(sa.DateTime)

    def __init__(self, arg):
        self.arg = arg
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.deleted_at = datetime.utcnow()