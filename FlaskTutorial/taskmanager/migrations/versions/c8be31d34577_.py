"""empty message

Revision ID: c8be31d34577
Revises: 9c74515b441f
Create Date: 2018-04-07 02:46:42.585816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8be31d34577'
down_revision = '9c74515b441f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['board.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_boards',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['board.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('desc', sa.String(length=1600), nullable=False),
    sa.Column('timestart', sa.DateTime(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('list_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['list_id'], ['list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_card_timestart'), 'card', ['timestart'], unique=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_index(op.f('ix_card_timestart'), table_name='card')
    op.drop_table('card')
    op.drop_table('user_boards')
    op.drop_table('list')
    op.drop_table('board')
    # ### end Alembic commands ###
