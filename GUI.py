import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

from gui_files.ui_menu import Ui_MainWindow as Ui_menu

from gui_files.ui_addPeople import Ui_MainWindow as Ui_addPeople

class Menu(QMainWindow, Ui_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_addPeople.clicked.connect(self.open_adder)

    def open_adder(self):
        adder = Adder()
        adder.show()
        sys.exit(adder.exec())


class Adder(QMainWindow, Ui_addPeople):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def startGUI():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    mainWindow = Menu()
    mainWindow.show()
    sys.exit(app.exec())
