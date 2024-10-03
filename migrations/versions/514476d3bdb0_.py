"""empty message

Revision ID: 514476d3bdb0
Revises: 21060e79509b
Create Date: 2024-10-01 22:53:45.720486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '514476d3bdb0'
down_revision = '21060e79509b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('departements', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))
        batch_op.drop_column('nom')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('departements', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nom', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###
