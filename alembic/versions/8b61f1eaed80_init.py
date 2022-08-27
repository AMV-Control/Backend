"""init

Revision ID: 8b61f1eaed80
Revises: 
Create Date: 2022-08-27 20:32:17.860511

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '8b61f1eaed80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('healthcheck',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('status', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('healthcheck')
    # ### end Alembic commands ###
