"""Run custom SQL script

Revision ID: 2460384ec6e5
Revises: 
Create Date: 2024-08-21 18:15:51.646292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2460384ec6e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    with open('database/clubmanager.sql', 'r') as file:
        sql = file.read()
    conn = op.get_bind()
    for statement in sql.split(';'):
        if statement.strip():
            conn.execute(sa.text(statement))


def downgrade():
    pass
