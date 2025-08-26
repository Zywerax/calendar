"""init

Revision ID: aeb3d1af1135
Revises: c77e76e6860c
Create Date: 2025-08-26 20:22:11.306272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aeb3d1af1135'
down_revision: Union[str, Sequence[str], None] = 'c77e76e6860c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
