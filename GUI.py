import sys
from datetime import date

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from People import People
from gui_files.ui_addPeople import Ui_Form as Ui_addPeople
from gui_files.ui_menu import Ui_MainWindow as Ui_menu
from gui_files.ui_settings import Ui_Settings as Ui_settings
from utilities import enable_high_resolution


class Menu(QMainWindow, Ui_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('aen_counter')
        self.btn_addPeople.clicked.connect(self.open_adder)
        self.win_addPeople = WidgetAddPeople(self)
        self.btn_settings.clicked.connect(self.open_settings)
        self.win_settings = WidgetSettings(self)
        self.wins = (self.win_settings, self.win_addPeople)

    def show_menu(self):
        self.show()
        for i in self.wins:
            i.close()

    def open_adder(self):
        self.win_addPeople.show()
        self.close()

    def open_settings(self):
        self.win_settings.show()
        self.close()


class WidgetAddPeople(QMainWindow, Ui_addPeople):
    def __init__(self, parent: Menu):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Добавить спортсмена')
        self.but_menu.clicked.connect(parent.show_menu)
        self.addButton.clicked.connect(self.press_button)

    def press_button(self):
        somebody = self.get_people()
        print(somebody.fullname, somebody.birthday, somebody.weight)

    def get_people(self):
        try:
            name = self.edit_surname.text().strip().capitalize()
            surname = self.edit_name.text().strip().capitalize()
            birthday = self.edit_birthday.text()
            weight = self.edit_weight.text()

            if not (name and surname):
                raise ValueError('Имя и фамилия не могут быть пустыми')
            if not (name.isalpha() and surname.isalpha()):
                raise ValueError('Имя и фамилия могут содержать только буквы')
            date_bufer = date(*list(map(int, birthday.split('.')))[::-1])
            if (date.today() < date_bufer or
                    date_bufer < date(1900, 1, 1)):
                raise ValueError('Невозможная дата рождения')
            if not weight:  # нужно добавить настройку обязательного веса
                raise ValueError('Вес не может быть пустым')
            if not weight.replace('.', '', 1).isdigit():
                raise ValueError('Вес может содержать только дробное число')
            self.statusbar.showMessage('Успешно')
            fullname = name + ' ' + surname
            return People(fullname, birthday, float(weight))

        except ValueError as ve:
            self.statusbar.showMessage(ve.__str__())


class WidgetSettings(QWidget, Ui_settings):
    def __init__(self, parent: Menu):
        super().__init__()
        self.setupUi(self)


def startGUI():
    enable_high_resolution()
    app = QApplication(sys.argv)
    win_main = Menu()
    win_main.show()
    sys.exit(app.exec())
