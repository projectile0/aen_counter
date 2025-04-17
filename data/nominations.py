import sqlalchemy as sa

from .db_session import SqlAlchemyBase

class Nomination(SqlAlchemyBase):
    __tablename__ = 'nominations'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    type = sa.Column(sa.Integer, nullable=False)
    athletes = sa.Column(sa.String, nullable=False)
    finished = sa.Column(sa.Integer, default=0)
