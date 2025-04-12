from data.athletes import Athlete
from data.db_session import create_session
from data.users import User

from forms import RegisterFormAthlete, RegisterFormUser


def db_add_user(form: RegisterFormUser):  # Принимает RegisterFormUser, добавляет пользователя в базу
    db_sess = create_session()
    user = User()
    user.username = form.username.data.strip()
    user.set_password(form.password.data)
    db_sess.add(user)
    db_sess.commit()


def db_add_athlete(form: RegisterFormAthlete):  # Принимает RegisterFormAthlete, добавляет спортсмена в базу
    db_sess = create_session()
    athlete = Athlete()
    athlete.name = form.name.data.strip().capitalize()
    athlete.surname = form.surname.data.strip().capitalize()
    athlete.birth_date = form.birth_date.data
    athlete.weight = form.weight.data
    athlete.league = form.league.data
    db_sess.add(athlete)
    db_sess.commit()
