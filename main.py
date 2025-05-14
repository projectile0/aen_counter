from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from data import db_session
from database import *
from forms import LoginForm
from forms import AddBattleForm
from database import db_add_battle
from data.battles import Battle
from data.athletes import Athlete
from sqlalchemy import orm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AKFJDPOQWEXOFIJC_SDJKQ'

db_session.global_init("db/database.db")
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Главная')


@app.route('/add_athlete', methods=['GET', 'POST'])
@login_required
def page_add_athlete():
    form = RegisterFormAthlete()
    if form.validate_on_submit():
        db_add_athlete(form)
        return redirect('/')
    return render_template('page_form.html', form=form, title='Добавить спортсмена')


@app.route('/reg_user', methods=['GET', 'POST'])
def reg_user():
    form = RegisterFormUser()
    if form.validate_on_submit():
        db_add_user(form)
        return redirect('/')
    return render_template('page_form.html', form=form, title='Регистрация')


@app.route('/nomination', methods=['GET', 'POST'])
@login_required
def nomination():
    db_sess = db_session.create_session()
    athletes = db_sess.query(Athlete).all()

    form = AddBattleForm()
    form.athlete_1.choices = [(a.id, f"{a.surname} {a.name}") for a in athletes]
    form.athlete_2.choices = [(a.id, f"{a.surname} {a.name}") for a in athletes]

    if form.validate_on_submit():
        db_add_battle(
            form.athlete_1.data,
            form.athlete_2.data,
            form.score_1.data,
            form.score_2.data
        )
        return redirect('/nomination')

    battles = db_sess.query(Battle).options(
        orm.joinedload(Battle.athlete1),
        orm.joinedload(Battle.athlete2)
    ).all()

    return render_template('nominat.html', form=form, battles=battles, title='Номинации')


@app.route('/athlets')
@login_required
def athlets():
    db_sess = db_session.create_session()

    sort_by = request.args.get('sort')
    sort_order = request.args.get('order')

    query = db_sess.query(Athlete)

    if sort_by == 'surname':
        if sort_order == 'asc':
            query = query.order_by(Athlete.surname.asc())
        else:
            query = query.order_by(Athlete.surname.desc())
    elif sort_by == 'weight':
        if sort_order == 'asc':
            query = query.order_by(Athlete.weight.asc())
        else:
            query = query.order_by(Athlete.weight.desc())
    elif sort_by == 'league':
        if sort_order == 'asc':
            query = query.order_by(Athlete.league.asc())
        else:
            query = query.order_by(Athlete.league.desc())

    athletes = query.all()
    return render_template('list_athlets.html', athletes=athletes, title='Атлеты')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
    return render_template('page_form.html', form=form, title='Вход')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
