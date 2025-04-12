import sqlalchemy as sa

from validators import string_validator
from .db_session import SqlAlchemyBase, create_session


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
from wtforms.validators import DataRequired, InputRequired, Length


class RegisterFormAthlete(FlaskForm):
    name = StringField('Имя', validators=[InputRequired(), Length(max=20, message='Недопустимая длинна(>20)'),
                                          string_validator])
    surname = StringField('Фамилия', validators=[InputRequired(), Length(max=20, message='Недопустимая длинна(>20)'),
                                                 string_validator])
    birth_date = DateField('Дата рождения', validators=[DataRequired()])
    weight = FloatField('Вес', validators=[InputRequired()])
    league = SelectField('Лига', choices=[(0, 'А'), (1, 'Б'), (2, 'C'), (3, 'О')], validators=[InputRequired()])
    submit = SubmitField('Добавить спортсмена')


def db_add_athlete(form: RegisterFormAthlete): # Принимает RegisterFormAthlete, добавляет спортсмена в базу
    db_sess = create_session()
    athlete = Athlete()
    athlete.name = form.name.data.strip().capitalize()
    athlete.surname = form.surname.data.strip().capitalize()
    athlete.birth_date = form.birth_date.data
    athlete.weight = form.weight.data
    athlete.league = form.league.data
    db_sess.add(athlete)
    db_sess.commit()
