"""del common fields

Revision ID: 536a8ee9b721
Revises: 6edb6e8a4523
Create Date: 2023-09-30 22:08:26.340885

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '536a8ee9b721'
down_revision: Union[str, None] = '6edb6e8a4523'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'faculty')
    op.drop_column('student', 'curse')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('curse', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('student', sa.Column('faculty', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###