"""init

Revision ID: b884a1addcdb
Revises: aeb3d1af1135
Create Date: 2025-08-26 20:24:17.200016

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b884a1addcdb'
down_revision: Union[str, Sequence[str], None] = 'aeb3d1af1135'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
