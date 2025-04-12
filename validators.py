from string import digits, ascii_letters

from wtforms import ValidationError

from data.db_session import create_session
from data.users import User


def string_validator(form, field): # Проверка на содержание только букв
    if not field.data.strip().isalpha():
        raise ValidationError('Допустимы только буквы')


def username_validator(form, field): # Проверка корректности имени пользователя
    username = field.data.strip()
    if not all(map(lambda x: x in ascii_letters + digits, username)):
        raise ValidationError('Допустимы только цифры и латиниские буквы')
    if not any(map(lambda x: x in ascii_letters, field.data.strip())):
        raise ValidationError('Необходима латинские буквы')


def exist_user(form, field): # Проверка на уже существующего пользователя
    db_sess = create_session()
    username = field.data.strip()
    if db_sess.query(User).filter(User.username == username).first():
        raise ValidationError('Такой пользователь уже существует')


def password_validator(form, field): # Проверка корректности пароля(Запрещены только пробелы)
    password = field.data
    if ' ' in password:
        raise ValidationError('Пароль не должен содержать пробелы')
