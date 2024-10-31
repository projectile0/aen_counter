import sys

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from gui_files.ui_addPeople import Ui_Form as Ui_addPeople
from gui_files.ui_menu import Ui_MainWindow as Ui_menu
from gui_files.ui_settings import Ui_Settings as Ui_settings
from utilities import enable_high_resolution
from People import get_people

class Menu(QMainWindow, Ui_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('aen_counter')
        self.btn_addPeople.clicked.connect(self.open_adder)
        self.win_addPeople = WidgetAddPeople(self)
        self.win_addPeople.setFixedSize(self.win_addPeople.size())
        self.btn_settings.clicked.connect(self.open_settings)
        self.win_settings = WidgetSettings(self)
        self.wins = (self, self.win_settings, self.win_addPeople)
        for i in self.wins:
            i.setFixedSize(i.size())
            i.setWindowIcon(QtGui.QIcon('./res/icon.png'))

    def show_menu(self):
        self.show()
        for i in self.wins[1:]:
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
        somebody = get_people(self)
        print(somebody.fullname, somebody.birthday, somebody.weight)


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
