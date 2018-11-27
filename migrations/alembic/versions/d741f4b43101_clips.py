"""clips

Revision ID: d741f4b43101
Revises: e18e02aa4938
Create Date: 2018-11-18 22:42:46.755114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd741f4b43101'
down_revision = 'e18e02aa4938'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'clips',
        sa.Column('clip_id', sa.String(255), primary_key=True),
        sa.Column('user_id', sa.String(255)),
        sa.Column('stream_id', sa.String(255)),
        sa.Column('time_in', sa.Float),
        sa.Column('time_out', sa.Float),
        sa.Column('media_key', sa.String(255)),
        sa.Column('_status', sa.Integer),
        sa.Column('_date_created', sa.DateTime),
    )


def downgrade():
    op.drop_table('clips')

