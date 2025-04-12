from wtforms import ValidationError
from string import digits, ascii_letters
from data.db_session import create_session
from data.users import User

def string_validator(form, field):
    if not field.data.strip().isalpha():
        raise ValidationError('Допустимы только буквы')

def username_validator(form, field):
    username = field.data.strip()
    if not all(map(lambda x: x in ascii_letters + digits, username)):
        raise ValidationError('Допустимы только цифры и латиниские буквы')
    if not any(map(lambda x: x in ascii_letters, field.data.strip())):
        raise ValidationError('Необходима латинские буквы')
    db_sess = create_session()
    if db_sess.query(User).filter(User.username == username).first():
        raise ValidationError('Такой пользователь уже существует')


def password_validator(form, field):
    password = field.data
    if ' '  in password:
        raise ValidationError('Пароль не должен содержать пробелы')