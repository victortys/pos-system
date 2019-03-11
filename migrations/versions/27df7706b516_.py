"""empty message

Revision ID: 27df7706b516
Revises: 5e0880c4c07a
Create Date: 2019-02-26 13:23:17.476029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27df7706b516'
down_revision = '5e0880c4c07a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('username', sa.String(length=60), nullable=True))
    op.create_index(op.f('ix_employees_username'), 'employees', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employees_username'), table_name='employees')
    op.drop_column('employees', 'username')
    # ### end Alembic commands ###