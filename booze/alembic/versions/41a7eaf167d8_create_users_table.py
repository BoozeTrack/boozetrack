"""create tables

Revision ID: 41a7eaf167d8
Revises: None
Create Date: 2012-07-10 23:07:12.069656

"""

# revision identifiers, used by Alembic.
revision = '41a7eaf167d8'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('user_id',  sa.CHAR(22),  primary_key=True),
        sa.Column('username', sa.String(80),  unique=True),
        sa.Column('email',    sa.String(120), unique=True),
        sa.Column('fb_id',    sa.BigInteger,  nullable=True, index=True),
        sa.Column('state',    sa.CHAR(2)),
    )
    op.create_table(
        'bottles',
        sa.Column('bottle_id', sa.CHAR(22),  primary_key=True),
        sa.Column('name',      sa.String(255)  ),
        sa.Column('upc',       sa.BigInteger   ),
        sa.Column('abv',       sa.SmallInteger ),
        sa.Column('maker_id',  sa.CHAR(22),  index=True),
        sa.Column('type_id',   sa.CHAR(22),  index=True),
        sa.Column('size_id',   sa.CHAR(22),  index=True),
        )
    op.create_table(
        'sizes',
        sa.Column('size_id', sa.CHAR(22),  primary_key=True),
        sa.Column('ml',      sa.SmallInteger ),
        sa.Column('oz',      sa.SmallInteger ),
    )
    op.create_table(
        'devices',
        sa.Column('device_id', sa.CHAR(22), primary_key=True),
        sa.Column('os',        sa.CHAR(1)     ),
        sa.Column('uuid',      sa.String(255) ),
    )
    op.create_table(
        'prices',
        sa.Column('user_id',   sa.CHAR(22)),
        sa.Column('bottle_id', sa.CHAR(22)),
        #price
        sa.Column('geohash',   sa.VARCHAR(22)),
        sa.Column('when',      sa.Integer), # timestamp rounded to nearest N minutes
        sa.PrimaryKeyConstraint('bottle_id', 'when', 'geohash', 'user_id'),
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('bottles')
    op.drop_table('sizes')
    op.drop_table('devices')
    op.drop_table('prices')
