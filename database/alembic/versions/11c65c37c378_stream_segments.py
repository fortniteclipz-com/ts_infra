"""stream_segments

Revision ID: 11c65c37c378
Revises: a132e85aa35a
Create Date: 2018-11-18 22:25:28.554447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11c65c37c378'
down_revision = 'a132e85aa35a'
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


def downgrade():
    op.drop_table('stream_segments')

