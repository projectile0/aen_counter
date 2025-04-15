from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from data import db_session
from database import *
from forms import LoginForm

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
def nomination():
    form = RegisterFormUser()
    if form.validate_on_submit():
        db_add_user(form)
        return redirect('/')
    return render_template('nomination.html', form=form, title='Регистрация')

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
