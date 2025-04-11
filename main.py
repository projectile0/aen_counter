from flask import Flask, render_template, request
from data import db_session
from forms.RegisterFormAthlete import RegisterFormAthlete
from forms.RegisterFormUser import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AKFJDPOQWEXOFIJC_SDJKQ'

@app.route('/')
def index():
    return 'Главная страница'

@app.route('/add_athlete', methods=['GET', 'POST'])
def add_athlete():
    form = RegisterFormAthlete()
    if request.method == 'GET':
        return render_template('add_athlete.html', form=form)
    else:
        return 'success'

@app.route('/reg_user', methods=['GET', 'POST'])
def reg_athlete():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register_athlete.html', form=form)
    else:
        return 'success'

def main():
    db_session.global_init("db/database.db")
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
