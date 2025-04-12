from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_required, login_user

from data import db_session
from forms import RegisterFormAthlete, LoginForm, RegisterFormUser
from data.users import User
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AKFJDPOQWEXOFIJC_SDJKQ'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/add_athlete', methods=['GET', 'POST'])
@login_required
def page_add_athlete():
    form = RegisterFormAthlete()
    if form.validate_on_submit():
        db_add_athlete(form)
        return redirect('/')
    return render_template('page_form.html', form=form)


@app.route('/reg_user', methods=['GET', 'POST'])
def reg_athlete():
    form = RegisterFormUser()
    if form.validate_on_submit():
        db_add_user(form)
        return redirect('/')
    return render_template('page_form.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return redirect('/')
    return render_template('page_form.html', form=form)





def main():
    db_session.global_init("db/database.db")
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        db_sess = db_session.create_session()
        return db_sess.query(User).get(user_id)

    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
