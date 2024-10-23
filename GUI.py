import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from gui_files.ui_addPeople import Ui_Form as Ui_addPeople
from gui_files.ui_menu import Ui_MainWindow as Ui_menu
from gui_files.ui_settings import Ui_Settings as Ui_settings
from utilities import enable_high_resolution
from datetime import date

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
        try:
            name, surname = self.edit_surname.text().strip().capitalize(), self.edit_name.text().strip().capitalize()
            date_born = self.edit_birthday.text()
            if not (name and surname):
                raise ValueError('Имя и фамилия не могут быть пустыми')
            if not (name.isalpha() and surname.isalpha()):
                raise ValueError('Имя и фамилия могут содержать только буквы')
            if date.today() < date(*list(map(int,date_born.split('.')))[::-1]):
                print(1)
                raise ValueError('Невозможная дата рождения')
            self.statusbar.showMessage('')
            fullname = name + ' ' + surname
            print(fullname)
            born = self.edit_birthday.text()
            print(date_born)
        except ValueError as ve:
            self.statusbar.showMessage(ve.__str__())


class WidgetSettings(QWidget, Ui_settings):
    def __init__(self, parent: Menu):
        super().__init__()
        self.setupUi(self)


def startGUI():
    enable_high_resolution()
    app = QApplication(sys.argv)
    mainWindow = Menu()
    mainWindow.show()
    sys.exit(app.exec())
