"""montage_clips

Revision ID: a85733cda3ea
Revises: 283e58e8dae6
Create Date: 2018-11-18 22:53:22.710420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a85733cda3ea'
down_revision = '283e58e8dae6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'montage_clips',
        sa.Column('montage_id', sa.String(255), primary_key=True),
        sa.Column('clip_id', sa.String(255), primary_key=True),
        sa.Column('clip_order', sa.Integer),
    )

    op.create_index(
        'montage_id:clip_order',
        'montage_clips',
        ['montage_id', 'clip_order'],
    )

def downgrade():
    op.drop_table('montage_clips')

