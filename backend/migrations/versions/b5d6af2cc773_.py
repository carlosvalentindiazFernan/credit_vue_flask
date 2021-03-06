"""empty message

Revision ID: b5d6af2cc773
Revises: e54aad24bb4c
Create Date: 2019-05-13 23:35:32.936157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5d6af2cc773'
down_revision = 'e54aad24bb4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('credit',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name_company', sa.String(length=255), nullable=False),
    sa.Column('num_company', sa.String(length=255), nullable=False),
    sa.Column('credit', sa.Float(), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('credit')
    # ### end Alembic commands ###
