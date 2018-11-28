"""montages

Revision ID: 283e58e8dae6
Revises: d741f4b43101
Create Date: 2018-11-18 22:50:35.932674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '283e58e8dae6'
down_revision = 'd741f4b43101'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'montages',
        sa.Column('montage_id', sa.String(255), primary_key=True),
        sa.Column('user_id', sa.String(255)),
        sa.Column('stream_id', sa.String(255)),
        sa.Column('streamer', sa.String(255)),
        sa.Column('duration', sa.Float),
        sa.Column('clips', sa.Integer),
        sa.Column('media_key', sa.String(255)),
        sa.Column('_status', sa.Integer),
        sa.Column('_date_created', sa.DateTime),
    )

    op.create_index(
        '_date_created',
        'montages',
        ['_date_created'],
    )

    op.create_index(
        'user_id:_date_created',
        'montages',
        ['user_id', '_date_created'],
    )


def downgrade():
    op.drop_table('montages')

