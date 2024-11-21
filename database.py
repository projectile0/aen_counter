import sqlite3

from person import Person


def db_connection():
    return sqlite3.connect('database.sqlite')


def get_filterArr(con, weight=None, year=None, league=None, surname=None):
    cur = con.cursor()
    return cur.execute('''SELECT * FROM athletes''').fetchall()


def add_person(con, person: Person):
    try:
        cur = con.cursor()
        req = f'''INSERT INTO athletes(name, weight, birthday, league) VALUES ('{person.fullname}', {person.weight},
                    '{person.birthday}', (SELECT id FROM leagues WHERE league = '{person.league}'))'''
        cur.execute(req)
        con.commit()
    except Exception as e:
        print(e)


def clear_database(parent):
    parent.db_con.close()
    with open('database.sqlite', 'w'):
        parent.db_con = sqlite3.connect('database.sqlite')
    parent.db_con.executescript(open('sql/create_athletes.sql').read())
    parent.db_con.executescript(open('sql/create_leagues.sql').read())
    parent.db_con.executescript(open('sql/create_athletes_nomination.sql').read())
    parent.db_con.executescript(open('sql/add_standart_leagues.sql').read())
