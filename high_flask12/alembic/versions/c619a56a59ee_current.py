"""'current'

Revision ID: c619a56a59ee
Revises: 55280f417a8d
Create Date: 2019-12-27 14:46:25.744265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c619a56a59ee'
down_revision = '55280f417a8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userinfo', sa.Column('age', sa.String(length=50), nullable=False))
    op.create_unique_constraint(None, 'userinfo', ['age'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'userinfo', type_='unique')
    op.drop_column('userinfo', 'age')
    # ### end Alembic commands ###
