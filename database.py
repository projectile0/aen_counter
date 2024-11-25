import sqlite3
from datetime import datetime

from person import Person


def db_connection():
    return sqlite3.connect('database.sqlite')


def get_filterArr(con, **filters):  # nomination=None, heavy_weight=None):
    filter_dict = {
        'weight': check_weight,
        'year': check_year,
        'league': check_league,
        'surname': check_surname,
        'weight_class': check_weight_class,
        'nomination': check_nomination,
        'age': check_age
    }
    cur = con.cursor()

    if "league" in filters.keys():  # Получение id лиги
        if filters["league"]:
            req = f'''SELECT id FROM leagues 
                            WHERE league = '{filters['league']}' '''
            league = cur.execute(req).fetchone()
            filters['league'] = league[0]
    sql_filters = []
    for i in filters.keys():  # добавление sql кода в список фильтров
        if filters[i]:
            sql_filters.append(filter_dict[i](filters[i]))
    where = ' and '.join(sql_filters)
    if where:
        where = 'WHERE ' + where
    req = f'''
        SELECT athletes.*,
           athletes_nomination.sh_n_saber,
           athletes_nomination.sh_n_sword,
           athletes_nomination.triathlon
        FROM athletes
                 LEFT JOIN athletes_nomination
                           on athletes.id = athletes_nomination.id
        {where}'''
    print(req)
    arr = cur.execute(req).fetchall()
    return arr


def check_weight(weight):  # возвращает sql для проверки соответствия веса с границами
    if weight:
        weight = weight.split('-')
        return f'{weight[0]} <= athletes.weight and athletes.weight <= {weight[1]}'
    return ''


def check_year(year):  # возвращает sql сравнивающий год с таблицей
    if year:
        return f'athletes.birthday LIKE "%{year}"'  # TODO Прописать в руководстве о возможности использования последних цифр
    return ''


def check_league(league):  # возвращает sql сравнивающий лигу с таблицей

    if league:
        return f'athletes.league = {league}'
    return ''


def check_surname(surname):  # возвращает sql сравнивающий имя и фамилию с таблицей
    if surname:
        return f'athletes.name LIKE "%{surname}%"'
    return ''


def check_weight_class(weight_class):
    critical_weight = 45
    if weight_class is not None:
        w_classes = {
            'Лёгкий': '<',
            'Тяжёлый': '>='
        }
        return f'athletes.weight {w_classes[weight_class]} {critical_weight}'
    return ''


def check_nomination(nomination):  # возвращает sql для проверки участия в номинации
    if nomination:
        noms = {
            'Меч+щит': 'sh_n_sword',
            'Сабля+щит': 'sh_n_saber',
            'Триатлон': 'triathlon'
        }
        return f'athletes_nomination.{noms[nomination]} = 1'
    return ''


def check_age(age):  # возвращает sql для проверки соответствия возраста с границами
    if age:
        cur_year = datetime.now().year
        age = age.split('-')
        print(cur_year - int(age[0]))
        return f' "{cur_year - int(age[1])}" <= substr(athletes.birthday, 7, 4) and substr(athletes.birthday, 7, 4) <= "{cur_year - int(age[0])}" '
    return ''


def add_person(con, person: Person):
    try:
        cur = con.cursor()
        req = f'''
            INSERT INTO athletes(name, weight, birthday, league)
            VALUES ('{person.fullname}', {person.weight},
                    '{person.birthday}', (SELECT id FROM leagues WHERE league = '{person.league}'))'''
        cur.execute(req)
        req = f'''
            INSERT INTO athletes_nomination(sh_n_saber, sh_n_sword, triathlon)
            VALUES ({person.s_n_saber}, {person.s_n_sword}, {person.triathlon})'''
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
