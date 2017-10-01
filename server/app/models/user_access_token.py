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
    def create(cls, user_id, with_refresh_token=False):
        expires = timedelta(days=7)
        access_token = create_access_token(identity=user_id, expires_delta=expires, fresh=with_refresh_token)
        cls.save_encoded_token(access_token)
        if with_refresh_token:
            refresh_token = create_refresh_token(identity=user_id)
            cls.save_encoded_token(refresh_token)
            return access_token, refresh_token
        return access_token

    @classmethod
    def save_encoded_token(cls, token):
        decoded_token = decode_token(token)
        user_id = decoded_token['identity']
        jti = decoded_token['jti']
        token_type = decoded_token['type']
        fresh = decoded_token.get('fresh', False)
        expires = datetime.fromtimestamp(decoded_token['exp'])
        return super().create(dict(user_id=user_id, jti=jti, token_type=token_type, fresh=fresh, expires=expires, encoded=token))

    @classmethod
    def is_token_blacklisted(cls, decoded_token):
        jti = decoded_token['jti']
        access_token = cls.query.filter_by(jti=jti).first()
        if access_token is None:
            return True
        is_deleted = access_token.deleted_at is not None
        return is_deleted

    @classmethod
    def add_token_to_blacklist(cls, jti):
        result = cls.query.filter_by(jti=jti).update(dict(deleted_at=datetime.utcnow()))
        sa.session.commit()
        return result
