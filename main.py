from flask import Flask


def main():
    app = Flask(__name__)

    @app.route('/')
    def main():
        return 'Главная страница'

    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
