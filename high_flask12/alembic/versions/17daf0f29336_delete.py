"""'delete'

Revision ID: 17daf0f29336
Revises: 4c4ef29d46d3
Create Date: 2019-12-27 15:25:00.120640

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '17daf0f29336'
down_revision = '4c4ef29d46d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userinfo', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userinfo', sa.Column('address', mysql.VARCHAR(length=100), nullable=False))
    # ### end Alembic commands ###
