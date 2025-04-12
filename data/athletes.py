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


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FloatField, SelectField
from wtforms.validators import DataRequired, InputRequired


class RegisterFormAthlete(FlaskForm):
    name = StringField('Имя', validators=[InputRequired()])
    surname = StringField('Фамилия', validators=[InputRequired()])
    birth_date = DateField('Дата рождения', validators=[DataRequired()])
    weight = FloatField('Вес', validators=[InputRequired()])
    league = SelectField('Лига', choices=[(0, 'А'), (1, 'Б'), (2, 'C'), (3, 'О')], validators=[DataRequired()])
    submit = SubmitField('Добавить спортсмена')
