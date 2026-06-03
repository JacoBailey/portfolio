"""add bullet ordering constraints

Revision ID: 817805639f4a
Revises: 1d01af01dd90
Create Date: 2026-06-02 17:43:07.710440

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '817805639f4a'
down_revision: Union[str, Sequence[str], None] = '1d01af01dd90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # MANUAL MIGRATION
    
    # 1. Rename table
    op.rename_table("experience", "experiences")

    # 2. Update foreign key constraint due to new tablename
    op.drop_constraint(op.f('experience_bullets_experience_id_fkey'), 'experience_bullets', type_='foreignkey')
    op.create_foreign_key('experience_bullets_experience_id_fkey', 'experience_bullets', 'experiences', ['experience_id'], ['id'])
    
    # 3. Add constraints
    op.create_unique_constraint('unique_experience_bullet_order', 'experience_bullets', ['experience_id', 'order_index'])
    op.create_unique_constraint('unique_project_bullet_order', 'project_bullets', ['project_id', 'order_index'])
    op.create_unique_constraint('unique_technical_bullet_order', 'technical_bullets', ['skill_id', 'order_index'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('unique_technical_bullet_order', 'technical_bullets', type_='unique')
    op.drop_constraint('unique_project_bullet_order', 'project_bullets', type_='unique')
    op.drop_constraint('unique_experience_bullet_order', 'experience_bullets', type_='unique')
    
    op.drop_constraint("experience_bullets_experience_id_fkey", 'experience_bullets', type_='foreignkey')
    op.create_foreign_key(op.f('experience_bullets_experience_id_fkey'), 'experience_bullets', 'experience', ['experience_id'], ['id'])
    
    op.rename_table("experiences", "experience")