"""v1

Revision ID: 7e8d57e44be
Revises: None
Create Date: 2015-08-27 13:34:49.727233

"""

# revision identifiers, used by Alembic.
revision = '7e8d57e44be'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=164), nullable=True),
    sa.Column('password_hash', sa.String(length=164), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=164), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('author', sa.Text(), nullable=True),
    sa.Column('tag', sa.String(length=164), nullable=True),
    sa.Column('summary', sa.Text(), nullable=True),
    sa.Column('image', sa.String(length=164), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('start', sa.String(length=164), nullable=True),
    sa.Column('end', sa.String(length=164), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('users')
    ### end Alembic commands ###
