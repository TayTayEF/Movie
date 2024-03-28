"""empty message

Revision ID: de54aba3efeb
Revises: 81c43a073935
Create Date: 2022-03-08 16:36:28.753343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de54aba3efeb'
down_revision = '81c43a073935'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'movieDB', ['movie_id'], ['movie_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
