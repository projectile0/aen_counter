from datetime import date


class Person:
    def __init__(self, fullname, birthday, weight, league, nominations):
        self.fullname = fullname
        self.birthday = birthday
        self.weight = weight
        self.league = league
        self.s_n_saber = nominations[0]
        self.s_n_sword = nominations[1]
        self.triathlon = nominations[2]

    def change_fullname(self, fullname):
        self.fullname = fullname

    def change_birthday(self, birthday):
        self.birthday = birthday

    def change_weight(self, new_weight):
        self.weight = new_weight


def get_person(self):
    try:
        name = self.edit_name.text().strip().capitalize()
        surname = self.edit_surname.text().strip().capitalize()
        birthday = self.edit_birthday.text()
        weight = self.edit_weight.text()
        leagues = [self.league_a, self.league_b, self.league_c, self.league_o]
        league = list(filter(lambda x: x.isChecked(), leagues))
        if not league:
            raise ValueError('Выберите лигу')
        league = league[0].text()
        nominations = self.check_saber.isChecked(), self.check_sword.isChecked(), self.check_triathlon.isChecked()
        nominations = (list(map(int, nominations)))
        if not (name and surname):
            raise ValueError('Имя и фамилия не могут быть пустыми')
        if not (name.isalpha() and surname.isalpha()):
            raise ValueError('Имя и фамилия могут содержать только буквы')
        date_buffer = date(*list(map(int, birthday.split('.')))[::-1])
        if (date.today() < date_buffer or
                date_buffer < date(1900, 1, 1)):
            raise ValueError('Невозможная дата рождения')
        if not weight:  # TODO нужно добавить настройку обязательного веса
            raise ValueError('Вес не может быть пустым')
        if not weight.replace('.', '', 1).isdigit():
            raise ValueError('Вес может содержать только дробное число')
        self.statusbar.showMessage(f'{surname} успешно добавлен')
        fullname = name + ' ' + surname
        return Person(fullname, birthday, round(float(weight), 2), league, nominations)

    except ValueError as ve:
        self.statusbar.showMessage(ve.__str__())
