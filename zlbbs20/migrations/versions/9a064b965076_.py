"""empty message

Revision ID: 9a064b965076
Revises: 186c6f0d376c
Create Date: 2020-03-02 07:25:03.779547

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9a064b965076'
down_revision = '186c6f0d376c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('front_user',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('telephone', sa.String(length=11), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('_password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('realname', sa.String(length=50), nullable=True),
    sa.Column('avatar', sa.String(length=100), nullable=True),
    sa.Column('signature', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.Enum('MALE', 'FEMALE', 'SECRET', 'UNKNOW', name='genderenum'), nullable=True),
    sa.Column('join_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('telephone')
    )
    op.create_table('CMS_User_Role',
    sa.Column('CMSRole_id', sa.Integer(), nullable=False),
    sa.Column('CMSUser_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['CMSRole_id'], ['cms_role.id'], ),
    sa.ForeignKeyConstraint(['CMSUser_id'], ['cms_user.id'], ),
    sa.PrimaryKeyConstraint('CMSRole_id', 'CMSUser_id')
    )
    op.drop_table('cms_user_role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cms_user_role',
    sa.Column('CMSRole_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('CMSUser_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['CMSRole_id'], ['cms_role.id'], name='cms_user_role_ibfk_1'),
    sa.ForeignKeyConstraint(['CMSUser_id'], ['cms_user.id'], name='cms_user_role_ibfk_2'),
    sa.PrimaryKeyConstraint('CMSRole_id', 'CMSUser_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('CMS_User_Role')
    op.drop_table('front_user')
    # ### end Alembic commands ###
