import sqlite3
from person import Person
def db_connection():
    return sqlite3.connect('database.sqlite')

def get_filterArr(con, weight=None, year=None, league=None, surname=None):
    cur = con.cursor()
    return cur.execute('''SELECT * FROM athletes''').fetchall()

def add_person(person):
    person