from flask import Flask, render_template, request, redirect

from data import db_session
from data.athletes import RegisterFormAthlete, db_add_athlete

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AKFJDPOQWEXOFIJC_SDJKQ'


@app.route('/')
def index():
    return 'Главная страница'


@app.route('/add_athlete', methods=['GET', 'POST'])
def page_add_athlete():
    form = RegisterFormAthlete()
    if request.method == 'GET':
        return render_template('page_add_athlete.html', form=form)
    else:
        if form.validate_on_submit():
            db_add_athlete(form)
            return redirect('/')
        return render_template('page_add_athlete.html', form=form)


def main():
    db_session.global_init("db/database.db")
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
