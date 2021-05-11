"""empty message

Revision ID: 3a851969dbd6
Revises: 
Create Date: 2021-05-11 19:59:03.592020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a851969dbd6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quizname', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('questiontext', sa.String(length=256), nullable=True),
    sa.Column('quizId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['quizId'], ['quiz.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quizid', sa.Integer(), nullable=True),
    sa.Column('topicname', sa.String(length=256), nullable=True),
    sa.Column('topicvideolink', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['quizid'], ['quiz.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answertext', sa.String(length=256), nullable=True),
    sa.Column('questionId', sa.Integer(), nullable=False),
    sa.Column('correctAnswer', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['questionId'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quiz_result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quizid', sa.Integer(), nullable=False),
    sa.Column('userresultid', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quizid'], ['quiz.id'], ),
    sa.ForeignKeyConstraint(['userresultid'], ['user_result.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topic_section',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topicid', sa.Integer(), nullable=False),
    sa.Column('topicheading', sa.String(length=256), nullable=True),
    sa.Column('topiccontent', sa.String(length=1024), nullable=True),
    sa.ForeignKeyConstraint(['topicid'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('topic_section')
    op.drop_table('quiz_result')
    op.drop_table('answer')
    op.drop_table('user_result')
    op.drop_table('topic')
    op.drop_table('question')
    op.drop_table('user')
    op.drop_table('quiz')
    # ### end Alembic commands ###