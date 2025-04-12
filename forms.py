from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, SelectField, FloatField, DateField
from wtforms.validators import Length, InputRequired, EqualTo, DataRequired

from validators import username_validator, password_validator, string_validator


class RegisterFormUser(FlaskForm):
    username = StringField('Имя пользователя', validators=[InputRequired(), Length(min=5, max=20), username_validator])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=40), password_validator])
    password_again = PasswordField('Повторите пароль',
                                   validators=[InputRequired(), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[InputRequired(), Length(min=5, max=20), username_validator])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=40), password_validator])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegisterFormAthlete(FlaskForm):
    name = StringField('Имя', validators=[InputRequired(), Length(max=20, message='Недопустимая длинна(>20)'),
                                          string_validator])
    surname = StringField('Фамилия', validators=[InputRequired(), Length(max=20, message='Недопустимая длинна(>20)'),
                                                 string_validator])
    birth_date = DateField('Дата рождения', validators=[DataRequired()])
    weight = FloatField('Вес', validators=[InputRequired()])
    league = SelectField('Лига', choices=[(0, 'А'), (1, 'Б'), (2, 'C'), (3, 'О')], validators=[InputRequired()])
    submit = SubmitField('Добавить спортсмена')