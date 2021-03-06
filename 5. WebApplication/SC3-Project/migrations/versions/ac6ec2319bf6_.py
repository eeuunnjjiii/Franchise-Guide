"""empty message

Revision ID: ac6ec2319bf6
Revises: a9b532e3303a
Create Date: 2021-06-01 23:57:14.640653

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ac6ec2319bf6'
down_revision = 'a9b532e3303a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('predict',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('업종', sa.String(length=45), nullable=True),
    sa.Column('브랜드', sa.String(length=45), nullable=True),
    sa.Column('가맹점수', sa.Integer(), nullable=True),
    sa.Column('초기투자비용합계', sa.Integer(), nullable=True),
    sa.Column('예상평균매출액', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('check', sa.Column('브랜드_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'check', 'project', ['브랜드_id'], ['id'])
    op.drop_column('check', '당기순이익')
    op.drop_column('check', '매출액')
    op.drop_column('check', '영업이익')
    op.drop_column('check', '부채')
    op.drop_column('check', '평가')
    op.drop_column('check', '기준연도')
    op.drop_column('check', '업종')
    op.drop_column('check', '자본')
    op.drop_column('check', '자산')
    op.drop_column('check', '명의변경')
    op.drop_column('check', '법위반횟수')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('check', sa.Column('법위반횟수', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('check', sa.Column('명의변경', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('check', sa.Column('자산', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('check', sa.Column('자본', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('check', sa.Column('업종', mysql.VARCHAR(length=45), nullable=True))
    op.add_column('check', sa.Column('기준연도', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('check', sa.Column('평가', mysql.VARCHAR(length=45), nullable=True))
    op.add_column('check', sa.Column('부채', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('check', sa.Column('영업이익', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('check', sa.Column('매출액', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('check', sa.Column('당기순이익', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'check', type_='foreignkey')
    op.drop_column('check', '브랜드_id')
    op.drop_table('predict')
    # ### end Alembic commands ###
