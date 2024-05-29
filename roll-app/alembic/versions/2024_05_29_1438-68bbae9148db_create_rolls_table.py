"""create rolls table

Revision ID: 68bbae9148db
Revises: 
Create Date: 2024-05-29 14:38:17.153474

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "68bbae9148db"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "rolls",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("length", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Integer(), nullable=False),
        sa.Column("data_deleted", sa.Date(), nullable=True),
        sa.Column(
            "data_added",
            sa.Date(),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_rolls")),
    )


def downgrade() -> None:
    op.drop_table("rolls")
