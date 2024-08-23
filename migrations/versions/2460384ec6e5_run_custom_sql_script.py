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
    # Drop all tables created by the upgrade
    op.execute('DROP TABLE IF EXISTS coach CASCADE')
    op.execute('DROP TABLE IF EXISTS team CASCADE')
    op.execute('DROP TABLE IF EXISTS player CASCADE')

    conn = op.get_bind()

    # Get a list of all tables
    inspector = sa.inspect(conn)
    tables = inspector.get_table_names()
    print(tables)
    # Drop each table
    for table in tables:
        op.drop_table(table)