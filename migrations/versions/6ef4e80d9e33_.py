"""empty message

Revision ID: 6ef4e80d9e33
Revises: 36c74d5a6a6d
Create Date: 2018-04-22 00:05:16.766270

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6ef4e80d9e33'
down_revision = '36c74d5a6a6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(unsigned=True), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('nickname', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('gender', mysql.TINYINT(), nullable=False),
    sa.Column('active', mysql.TINYINT(), nullable=False),
    sa.Column('manager', mysql.TINYINT(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###