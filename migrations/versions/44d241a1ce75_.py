"""empty message

Revision ID: 44d241a1ce75
Revises: 9d7a17ababef
Create Date: 2024-02-29 17:45:27.631077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44d241a1ce75'
down_revision = '9d7a17ababef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_log_in', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('is_email_verify', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('is_phone_verify', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('is_phone_verify')
        batch_op.drop_column('is_email_verify')
        batch_op.drop_column('is_log_in')

    # ### end Alembic commands ###
