"""empty message

Revision ID: 2672720d4f49
Revises: b2d7e9f4f192
Create Date: 2020-03-27 14:30:25.383238

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2672720d4f49'
down_revision = 'b2d7e9f4f192'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'public_id',
               existing_type=postgresql.UUID(),
               type_=sa.String(length=50),
               existing_nullable=True)
    op.drop_constraint('users_public_id_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_public_id_key', 'users', ['public_id'])
    op.alter_column('users', 'public_id',
               existing_type=sa.String(length=50),
               type_=postgresql.UUID(),
               existing_nullable=True)
    # ### end Alembic commands ###
