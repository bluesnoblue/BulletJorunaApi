"""empty message

Revision ID: f85a5e054982
Revises: 
Create Date: 2019-08-05 20:49:57.161660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f85a5e054982'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=True),
    sa.Column('account', sa.String(length=16), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admin_users_account'), 'admin_users', ['account'], unique=True)
    op.create_index(op.f('ix_admin_users_description'), 'admin_users', ['description'], unique=True)
    op.create_index(op.f('ix_admin_users_name'), 'admin_users', ['name'], unique=True)
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['permissions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_roles_name'), 'roles', ['name'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=16), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('mobile', sa.String(length=11), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_mobile'), 'users', ['mobile'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('bullet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('bullet_type', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=32), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bullet_timestamp'), 'bullet', ['timestamp'], unique=False)
    op.create_table('role_permission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('to_do',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=32), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('to_do')
    op.drop_table('role_permission')
    op.drop_index(op.f('ix_bullet_timestamp'), table_name='bullet')
    op.drop_table('bullet')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_mobile'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_roles_name'), table_name='roles')
    op.drop_table('roles')
    op.drop_table('permissions')
    op.drop_index(op.f('ix_admin_users_name'), table_name='admin_users')
    op.drop_index(op.f('ix_admin_users_description'), table_name='admin_users')
    op.drop_index(op.f('ix_admin_users_account'), table_name='admin_users')
    op.drop_table('admin_users')
    # ### end Alembic commands ###