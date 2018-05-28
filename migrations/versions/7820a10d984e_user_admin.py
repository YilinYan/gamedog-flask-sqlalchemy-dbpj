"""user admin

Revision ID: 7820a10d984e
Revises: 6e076355923e
Create Date: 2018-05-10 14:38:50.377244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7820a10d984e'
down_revision = '6e076355923e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'admin')
    # ### end Alembic commands ###
