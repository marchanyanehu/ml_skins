"""Add MetaItem table

Revision ID: ca3226ff5d87
Revises: 81d00fc204e4
Create Date: 2024-10-23 23:46:02.162903

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca3226ff5d87'
down_revision: Union[str, None] = '81d00fc204e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meta_item',
    sa.Column('market_hash_name', sa.String(), nullable=False),
    sa.Column('popularity_7d', sa.Integer(), nullable=True),
    sa.Column('avg_price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('market_hash_name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('meta_item')
    # ### end Alembic commands ###
