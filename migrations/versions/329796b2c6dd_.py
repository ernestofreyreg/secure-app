"""empty message

Revision ID: 329796b2c6dd
Revises: 6e54102189c3
Create Date: 2022-05-20 00:21:34.375257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '329796b2c6dd'
down_revision = '6e54102189c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    # ### end Alembic commands ###
