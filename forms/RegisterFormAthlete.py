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
