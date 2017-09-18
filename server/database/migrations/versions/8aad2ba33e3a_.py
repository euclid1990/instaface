"""empty message

Revision ID: 8aad2ba33e3a
Revises: 
Create Date: 2017-09-13 09:48:14.980099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8aad2ba33e3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('gender', sa.SmallInteger(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('about', sa.Text(length=500), nullable=True),
    sa.Column('active_token', sa.String(length=255), nullable=True),
    sa.Column('jwt_token', sa.Text(length=300), nullable=True),
    sa.Column('password_changed_at', sa.DateTime(), nullable=True),
    sa.Column('logged_in_at', sa.DateTime(), nullable=True),
    sa.Column('logged_out_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###