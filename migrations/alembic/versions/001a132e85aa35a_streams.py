"""streams

Revision ID: 001a132e85aa35a
Revises:
Create Date: 2018-11-18 21:12:07.418523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001a132e85aa35a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'streams',
        sa.Column('stream_id', sa.String(255), primary_key=True),
        sa.Column('streamer', sa.String(255)),
        sa.Column('playlist_url', sa.String(255)),
        sa.Column('duration', sa.Float),
        sa.Column('width', sa.Integer),
        sa.Column('height', sa.Integer),
        sa.Column('fps_numerator', sa.Integer),
        sa.Column('fps_denominator', sa.Integer),
        sa.Column('game', sa.String(255)),
        sa.Column('_status_initialize', sa.Integer),
        sa.Column('_status_analyze', sa.Integer),
        sa.Column('_date_created', sa.DateTime),
    )

    op.create_index(
        '_status_analyze:_date_created',
        'streams',
        ['_status_analyze', '_date_created'],
    )


def downgrade():
    op.drop_table('streams')

