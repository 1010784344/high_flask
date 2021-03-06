"""'add'

Revision ID: 4c4ef29d46d3
Revises: c619a56a59ee
Create Date: 2019-12-27 15:22:01.430420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c4ef29d46d3'
down_revision = 'c619a56a59ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userinfo', sa.Column('address', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userinfo', 'address')
    # ### end Alembic commands ###
