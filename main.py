from flask import Flask, render_template
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AKFJDPOQWEXOFIJC_SDJKQ'

@app.route('/')
def index():
    return render_template('base.html')


def main():
    db_session.global_init("db/database.db")
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
