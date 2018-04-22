"""empty message

Revision ID: 3060be082bd4
Revises: 
Create Date: 2018-04-21 15:11:14.843934

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3060be082bd4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(unsigned=True), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('nickname', mysql.VARCHAR(length=128), nullable=False),
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
