

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FloatField, SelectField
from wtforms.validators import DataRequired

class RegisterFormAthlete(FlaskForm):

    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    birth_date = DateField('Дата рождения', validators=[DataRequired()])
    weight = FloatField('Вес', validators=[DataRequired()])
    league = SelectField('Лига', choices=[(0, 'А'), (1, 'Б'), (2, 'C'), (3, 'О')], validators=[DataRequired()]) # TODO Подключить radio button
    submit = SubmitField('Добавить спортсмена')