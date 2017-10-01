from app import sa, create_access_token, create_refresh_token
from datetime import datetime, timedelta
from marshmallow_sqlalchemy import ModelSchema
from flask_jwt_extended import decode_token
from .base import (Base, Mixin)

class UserAccessToken(Base, Mixin):

    __tablename__ = 'user_access_tokens'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, nullable=False)
    jti = sa.Column(sa.String(36), nullable=False, unique=True, index=True)
    token_type = sa.Column(sa.String(10), nullable=False)
    expires = sa.Column(sa.DateTime, nullable=False)
    fresh = sa.Column(sa.Boolean, default=False)
    encoded = sa.Column(sa.Text(300), nullable=False)

    __table_args__ = (
        sa.Index('ix_user_access_tokens_user_id_jti', 'user_id', 'jti'),
    )

    fillable = ['user_id', 'jti', 'token_type', 'expires', 'fresh', 'encoded']
    output = ('id', 'user_id', 'encoded')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def set_schema(cls):
        cls.schema = UserAccessTokenSchema

    @classmethod
    def create(cls, user_id):
        expires = timedelta(days=7)
        access_token = create_access_token(identity=user_id, expires_delta=expires, fresh=True)
        refresh_token = create_refresh_token(identity=user_id)
        decoded_token = decode_token(access_token)
        jti = decoded_token['jti']
        token_type = decoded_token['type']
        fresh = decoded_token['fresh']
        expires = datetime.fromtimestamp(decoded_token['exp'])
        super().create(dict(user_id=user_id, jti=jti, token_type=token_type, fresh=fresh, expires=expires, encoded=access_token))
        return access_token, refresh_token

    @classmethod
    def is_token_blacklisted(cls, decoded_token):
        jti = decoded_token['jti']
        access_token = cls.query.filter_by(jti=jti).first()
        if access_token is None:
            return True
        is_deleted = access_token.deleted_at is not None
        return is_deleted
