import sqlalchemy as sa
from datetime import datetime
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Battle(SqlAlchemyBase):
    __tablename__ = 'battles'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    athlete_1 = sa.Column(sa.Integer, sa.ForeignKey('athletes.id'))
    athlete_2 = sa.Column(sa.Integer, sa.ForeignKey('athletes.id'))
    score_1 = sa.Column(sa.Integer)
    score_2 = sa.Column(sa.Integer)
    time = sa.Column(sa.DateTime, default=datetime.now)

    athlete1 = orm.relationship("Athlete", foreign_keys=[athlete_1])
    athlete2 = orm.relationship("Athlete", foreign_keys=[athlete_2])
