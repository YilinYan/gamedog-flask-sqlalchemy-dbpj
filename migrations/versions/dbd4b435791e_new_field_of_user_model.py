"""new field of user model

Revision ID: dbd4b435791e
Revises: 19ded2acf348
Create Date: 2018-04-30 22:52:25.525452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbd4b435791e'
down_revision = '19ded2acf348'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('introduction', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'introduction')
    # ### end Alembic commands ###
