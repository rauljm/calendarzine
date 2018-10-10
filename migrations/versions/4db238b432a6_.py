"""empty message

Revision ID: 4db238b432a6
Revises: 041b908f283e
Create Date: 2018-10-10 20:39:51.876709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4db238b432a6'
down_revision = '041b908f283e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('schedule', sa.Column('room_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'schedule', 'room', ['room_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'schedule', type_='foreignkey')
    op.drop_column('schedule', 'room_id')
    op.drop_table('room')
    # ### end Alembic commands ###
