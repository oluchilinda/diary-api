"""confirmed feature added 1

Revision ID: 9d7aecacb243
Revises: 087be5e66402
Create Date: 2020-08-09 19:47:04.908991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d7aecacb243'
down_revision = '087be5e66402'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed_on')
    # ### end Alembic commands ###
