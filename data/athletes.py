import sqlalchemy as sa
from .db_session import SqlAlchemyBase

class Athlete(SqlAlchemyBase):
    __tablename__ = 'athletes'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    surname = sa.Column(sa.String, nullable=False)
    birth_date = sa.Column(sa.Date, nullable=False)
    weight = sa.Column(sa.Float)
    league = sa.Column(sa.Integer)