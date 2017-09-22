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

    schema = None
    fillable = []
    output = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.fillable:
                setattr(self, key, value)

    # Serializing objects (“Dumping”)
    @classmethod
    def dump(cls, Schema, obj, only=()):
        schema = Schema(only=only)
        print(schema)
        result = schema.dump(obj)
        return result.data

    @classmethod
    def json(cls, object):
        return cls.dump(cls.schema, object, cls.output)

class Mixin(object):
    # Create new record
    @classmethod
    def create(cls, data):
        data = dict((key, value) for (key, value) in data.items() if (key in cls.fillable))
        record = cls(**data)
        sa.session.add(record)
        sa.session.commit()
        return record

    # Update record by id
    @classmethod
    def updateById(cls, id, data):
        data.update(dict(updated_at=datetime.utcnow()))
        result = cls.query.filter_by(id=1).update(data)
        sa.session.commit()
        return result

    @staticmethod
    def _before_insert(mapper, connection, target):
        # print("Hook before insert")
        pass

    @classmethod
    def __declare_last__(cls):
        # print("Define hook occurs after mappings are assumed to be completed")
        event.listen(cls, 'before_insert', cls._before_insert)
