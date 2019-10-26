"""Rename 'user' table to 'users'

Revision ID: d9b81d8f5bbd
Revises: 189822528114
Create Date: 2019-10-26 11:48:35.118336

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd9b81d8f5bbd'
down_revision = '189822528114'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('user', 'users')


def downgrade():
    op.rename_table('users', 'user')
