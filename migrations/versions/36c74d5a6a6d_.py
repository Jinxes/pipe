"""empty message

Revision ID: 36c74d5a6a6d
Revises: b888f57ce061
Create Date: 2018-04-22 00:03:51.729535

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '36c74d5a6a6d'
down_revision = 'b888f57ce061'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=64), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
