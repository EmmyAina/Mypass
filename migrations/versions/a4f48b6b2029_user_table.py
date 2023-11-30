"""user table

Revision ID: a4f48b6b2029
Revises: 
Create Date: 2023-11-30 17:21:58.282759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4f48b6b2029'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.alter_column('account_name',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=70),
               existing_nullable=True)
        batch_op.alter_column('site_email',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=70),
               existing_nullable=False)
        batch_op.alter_column('site_password',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('site_name',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=70),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=70),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.String(length=70),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=70),
               existing_nullable=False)
        batch_op.alter_column('image_file',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('image_file',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=70),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.String(length=70),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=70),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.alter_column('site_name',
               existing_type=sa.String(length=70),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('site_password',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=60),
               existing_nullable=False)
        batch_op.alter_column('site_email',
               existing_type=sa.String(length=70),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('account_name',
               existing_type=sa.String(length=70),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)

    # ### end Alembic commands ###
