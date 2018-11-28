"""stream_moments

Revision ID: 003e18e02aa4938
Revises: 00211c65c37c378
Create Date: 2018-11-18 22:30:04.222777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003e18e02aa4938'
down_revision = '00211c65c37c378'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stream_moments',
        sa.Column('stream_moment_id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('stream_id', sa.String(255)),
        sa.Column('segment', sa.Integer),
        sa.Column('time', sa.Float),
        sa.Column('tag', sa.String(255)),
    )

    op.create_index(
        'stream_id:time',
        'stream_moments',
        ['stream_id', 'time'],
    )

def downgrade():
    op.drop_table('stream_moments')

