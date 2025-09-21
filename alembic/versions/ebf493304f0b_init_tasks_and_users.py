"""init tasks and users tables"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'init_tasks_and_users'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False, unique=True, index=True),
        sa.Column('password', sa.String, nullable=False)
    )

    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('completed', sa.Boolean, default=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'))
    )


def downgrade() -> None:
    op.drop_table('tasks')
    op.drop_table('users')
