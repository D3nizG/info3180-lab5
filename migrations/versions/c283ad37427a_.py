"""empty message

Revision ID: c283ad37427a
Revises: b1276bbc01c5
Create Date: 2021-03-08 21:14:28.851653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c283ad37427a'
down_revision = 'b1276bbc01c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'user_profiles', ['password'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_profiles', type_='unique')
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
