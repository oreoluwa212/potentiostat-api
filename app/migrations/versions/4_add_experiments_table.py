"""Add experiments table

Revision ID: b0cbd40923b6
Revises: 39e8ef751e4a
Create Date: 2024-03-10 21:47:41.505995

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b0cbd40923b6'
down_revision = '39e8ef751e4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('experiments',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_on', sa.DateTime(), nullable=False),
                    sa.Column('updated_on', sa.DateTime(), nullable=True),
                    sa.Column('is_deleted', sa.Boolean(), nullable=False),
                    sa.Column('experiment_status', sa.String(), nullable=False),
                    sa.Column('start_voltage', sa.DECIMAL(precision=9, scale=7), nullable=False),
                    sa.Column('end_voltage', sa.DECIMAL(precision=9, scale=7), nullable=False),
                    sa.Column('voltage_step', sa.DECIMAL(precision=9, scale=7), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('client_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_experiments_id'), 'experiments', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_experiments_id'), table_name='experiments')
    op.drop_table('experiments')
    # ### end Alembic commands ###