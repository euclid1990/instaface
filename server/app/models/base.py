from app import sa
from sqlalchemy import event
from datetime import datetime

class Base(sa.Model):
    # Skip the production of a table or mapper for the class entirely
    __abstract__ = True

    created_at = sa.Column(sa.DateTime(), default=datetime.utcnow)
    created_at._creation_order=997
    updated_at = sa.Column(sa.DateTime(), default=datetime.utcnow)
    updated_at._creation_order=998
    deleted_at = sa.Column(sa.DateTime())
    deleted_at._creation_order=999

    fillable = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.fillable:
                setattr(self, key, value)

class Mixin(object):
    # Update record by id
    @classmethod
    def updateById(cls, id, data):
        data.update(dict(updated_at=datetime.utcnow()))
        return cls.query.filter_by(id=1).update(data)

    @staticmethod
    def _before_insert(mapper, connection, target):
        print("Hook before insert")

    @classmethod
    def __declare_last__(cls):
        print("Define hook occurs after mappings are assumed to be completed")
        event.listen(cls, 'before_insert', cls._before_insert)
