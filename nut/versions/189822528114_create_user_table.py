"""create user table

Revision ID: 189822528114
Revises: 
Create Date: 2019-10-24 10:45:59.705342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '189822528114'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('user')
