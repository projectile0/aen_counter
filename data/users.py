import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase, create_session


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String, nullable=False, unique=True)
    hashed_password = sa.Column(sa.String, nullable=False)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import Length, InputRequired, EqualTo
from validators import username_validator, password_validator


class RegisterFormUser(FlaskForm):
    username = StringField('Имя пользователя', validators=[InputRequired(), Length(min=5, max=20), username_validator])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=40), password_validator])
    password_again = PasswordField('Повторите пароль',
                                   validators=[InputRequired(), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Войти')


def db_add_user(form: RegisterFormUser):  # Принимает RegisterFormAthlete, добавляет спортсмена в базу
    db_sess = create_session()
    user = User()
    user.username = form.username.data.strip()
    user.set_password(form.password.data)
    db_sess.add(user)
    db_sess.commit()
