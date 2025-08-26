"""init

Revision ID: 815e62591a3d
Revises: b884a1addcdb
Create Date: 2025-08-26 20:24:27.536741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '815e62591a3d'
down_revision: Union[str, Sequence[str], None] = 'b884a1addcdb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
