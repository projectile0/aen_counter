from wtforms import ValidationError

def string_validator(form, field):
    if not field.data.strip().isalpha():
        raise ValidationError('Допустимы только буквы')