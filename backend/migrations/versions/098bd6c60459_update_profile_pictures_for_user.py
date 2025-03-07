"""Update profile pictures for User

Revision ID: 098bd6c60459
Revises: 29bb57e773ea
Create Date: 2025-03-05 15:47:44.213785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '098bd6c60459'
down_revision = '29bb57e773ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_picture', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('profile_picture')

    # ### end Alembic commands ###
