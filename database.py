from data.athletes import Athlete
from data.db_session import create_session
from data.nominations import Nomination
from data.users import User
from data.battles import Battle

from forms import RegisterFormAthlete, RegisterFormUser


def db_add_user(form: RegisterFormUser):
    db_sess = create_session()
    user = User()
    user.username = form.username.data.strip()
    user.set_password(form.password.data)
    db_sess.add(user)
    db_sess.commit()


def db_add_athlete(form: RegisterFormAthlete):
    db_sess = create_session()
    athlete = Athlete()
    athlete.name = form.name.data.strip().capitalize()
    athlete.surname = form.surname.data.strip().capitalize()
    athlete.birth_date = form.birth_date.data
    athlete.weight = form.weight.data
    athlete.league = form.league.data
    db_sess.add(athlete)
    db_sess.commit()


def db_add_nomination(form):
    db_sess = create_session()
    nomination = Nomination()


def db_add_battle(athlete_1_id, athlete_2_id, score_1, score_2):
    db_sess = create_session()
    battle = Battle()
    battle.athlete_1 = athlete_1_id
    battle.athlete_2 = athlete_2_id
    battle.score_1 = score_1
    battle.score_2 = score_2
    db_sess.add(battle)
    db_sess.commit()