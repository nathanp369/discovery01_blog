"""20181122_v2

Revision ID: e41eec150053
Revises: d612dd55c66b
Create Date: 2018-11-24 23:49:24.206309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e41eec150053'
down_revision = 'd612dd55c66b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts','timestamp',new_column_name='create_timestamp')
    op.add_column('posts', sa.Column('edit_timestamp', sa.DateTime(), nullable=True))
    # op.create_index(op.f('ix_posts_create_timestamp'), 'posts', ['create_timestamp'], unique=False)
    op.create_index(op.f('ix_posts_edit_timestamp'), 'posts', ['edit_timestamp'], unique=False)
    # op.drop_index('ix_posts_timestamp', table_name='posts')
    # op.drop_column('posts', 'timestamp')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts','create_timestamp',new_column_name='timestamp')
    op.drop_index(op.f('ix_posts_edit_timestamp'), table_name='posts')
    op.drop_column('posts', 'edit_timestamp')
    # ### end Alembic commands ###
