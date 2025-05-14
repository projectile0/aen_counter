from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, SelectField, FloatField, DateField, IntegerField
from wtforms.validators import Length, InputRequired, EqualTo, DataRequired

from validators import username_validator, password_validator, string_validator, exist_user


class RegisterFormUser(FlaskForm): # Форма регистрации
    username = StringField('Имя пользователя',
                           validators=[InputRequired(), Length(min=5, max=20), username_validator, exist_user])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=40), password_validator])
    password_again = PasswordField('Повторите пароль',
                                   validators=[InputRequired(), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm): # Форма авторизации
    username = StringField('Имя пользователя', validators=[InputRequired(), Length(min=5, max=20), username_validator])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=40), password_validator])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterFormAthlete(FlaskForm): # Форма добавления спортсмена
    name = StringField('Имя', validators=[InputRequired(), Length(max=20, message='Недопустимая длинна(>20)'),
                                          string_validator])
    surname = StringField('Фамилия', validators=[InputRequired(), Length(max=20, message='Недопустимая длинна(>20)'),
                                                 string_validator])
    birth_date = DateField('Дата рождения', validators=[DataRequired()])
    weight = FloatField('Вес', validators=[InputRequired()])
    league = SelectField('Лига', choices=[(0, 'А'), (1, 'Б'), (2, 'C'), (3, 'О')], validators=[InputRequired()])
    submit = SubmitField('Добавить спортсмена')


class AddBattleForm(FlaskForm): # Форма добавления битвы
    athlete_1 = SelectField('Атлет 1', coerce=int, validators=[InputRequired()])
    athlete_2 = SelectField('Атлет 2', coerce=int, validators=[InputRequired()])
    score_1 = IntegerField('Счет атлета 1', validators=[InputRequired()])
    score_2 = IntegerField('Счет атлета 2', validators=[InputRequired()])
    submit = SubmitField('Добавить бой')
