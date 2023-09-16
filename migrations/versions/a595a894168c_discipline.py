"""Discipline

Revision ID: a595a894168c
Revises: 002d969d4eb7
Create Date: 2023-09-12 20:01:06.549920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a595a894168c'
down_revision: Union[str, None] = '002d969d4eb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('discipline', sa.Column('student_id', sa.Uuid(), nullable=False))
    op.create_foreign_key(None, 'discipline', 'student', ['student_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'discipline', type_='foreignkey')
    op.drop_column('discipline', 'student_id')
    # ### end Alembic commands ###
