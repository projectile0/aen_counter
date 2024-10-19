import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from gui_files.ui_addPeople import Ui_Form as Ui_addPeople
from gui_files.ui_menu import Ui_MainWindow as Ui_menu


class Menu(QMainWindow, Ui_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('aen_counter')
        self.btn_addPeople.clicked.connect(self.open_adder)
        self.win_addPeople = AddPeople(self)

    def show_menu(self):
        self.show()

    def open_adder(self):
        self.win_addPeople.show()


class AddPeople(QWidget, Ui_addPeople):
    def __init__(self, parent: Menu):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Добавить спортсмена')
        self.but_menu.clicked.connect(parent.show_menu)


def startGUI():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    mainWindow = Menu()
    mainWindow.show()
    sys.exit(app.exec())
