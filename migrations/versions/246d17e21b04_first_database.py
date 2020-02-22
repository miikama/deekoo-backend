"""first database

Revision ID: 246d17e21b04
Revises: 
Create Date: 2020-02-22 11:27:16.338411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '246d17e21b04'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=320), nullable=True),
    sa.Column('api_auth_token', sa.String(length=255), nullable=True),
    sa.Column('map_auth_token', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_api_auth_token'), 'users', ['api_auth_token'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_map_auth_token'), 'users', ['map_auth_token'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_map_auth_token'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_api_auth_token'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
