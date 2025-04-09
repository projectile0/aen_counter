from flask import Flask
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AKFJDPOQWEXOFIJC_SDJKQ'

@app.route('/')
def index():
    return 'Главная страница'


def main():
    db_session.global_init("db/database.db")
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
