"""users and news tables

Revision ID: 81bfa5ba7d06
Revises: 
Create Date: 2020-04-09 13:57:06.034879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81bfa5ba7d06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('published', sa.DateTime(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('role', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_role'), 'user', ['role'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_role'), table_name='user')
    op.drop_table('user')
    op.drop_table('news')
    # ### end Alembic commands ###
