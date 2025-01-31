"""stream_segments

Revision ID: 00211c65c37c378
Revises: 001a132e85aa35a
Create Date: 2018-11-18 22:25:28.554447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00211c65c37c378'
down_revision = '001a132e85aa35a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stream_segments',
        sa.Column('stream_id', sa.String(255), primary_key=True),
        sa.Column('segment', sa.Integer, primary_key=True),
        sa.Column('stream_time_in', sa.Float),
        sa.Column('stream_time_out', sa.Float),
        sa.Column('media_url', sa.String(255)),
        sa.Column('media_key', sa.String(255)),
        sa.Column('_status_download', sa.Integer),
        sa.Column('_status_analyze', sa.Integer),
    )

    op.create_index(
        'stream_id',
        'stream_segments',
        ['stream_id'],
    )

    op.create_index(
        'stream_id:stream_time_in:stream_time_out:segment',
        'stream_segments',
        ['stream_id', 'stream_time_in', 'stream_time_out', 'segment'],
    )


def downgrade():
    op.drop_table('stream_segments')

