"""empty message

Revision ID: 623e7f8a5e17
Revises: 
Create Date: 2021-05-30 11:20:56.074574

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '623e7f8a5e17'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('check',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('브랜드', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('project', '브랜드',
               existing_type=mysql.VARCHAR(length=45),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project', '브랜드',
               existing_type=mysql.VARCHAR(length=45),
               nullable=True)
    op.drop_table('check')
    # ### end Alembic commands ###