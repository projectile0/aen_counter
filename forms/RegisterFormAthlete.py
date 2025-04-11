from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FloatField, RadioField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    birth_date = DateField('Дата рождения', validators=[DataRequired()])
    weight = FloatField('Вес', validators=[DataRequired()])
    league = RadioField('Лига', validators=[DataRequired()]) # TODO Подключить radio button
    submit = SubmitField('Войти')