"""Added date added

Revision ID: 989fe77d9f92
Revises: 0a214e680172
Create Date: 2025-02-26 17:00:16.335046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '989fe77d9f92'
down_revision = '0a214e680172'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('practice_cases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_added', sa.DateTime(timezone=True), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('practice_cases', schema=None) as batch_op:
        batch_op.drop_column('date_added')

    # ### end Alembic commands ###
