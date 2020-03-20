"""empty message

Revision ID: e216f201cdc6
Revises: 5a777d5b01f6
Create Date: 2020-03-12 16:11:44.401620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e216f201cdc6'
down_revision = '5a777d5b01f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('banner',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=False),
    sa.Column('link_url', sa.String(length=255), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('creat_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('banner')
    # ### end Alembic commands ###