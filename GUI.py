import sys

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox, QFileDialog

from database import db_connection, get_filterArr, add_person, clear_database
from gui_files.ui_addPeople import Ui_Form as Ui_addPeople
from gui_files.ui_athletes import Ui_MainWindow as Ui_athletes
from gui_files.ui_menu import Ui_MainWindow as Ui_menu
from gui_files.ui_nomination_dialog import Ui_Dialog as Ui_nomination_dialog
from gui_files.ui_nominations import Ui_MainWindow as Ui_nominations
from gui_files.ui_settings import Ui_MainWindow as Ui_settings
from person import get_person
from utilities import enable_high_resolution


class Menu(QMainWindow, Ui_menu):
    def __init__(self):
        self.db_con = db_connection()
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('aen_counter')
        self.btn_addPeople.clicked.connect(self.open_adder)  # Создание окон и привязка кнопок в меню к их открытию
        self.win_addPeople = WidgetAddPeople(self)
        self.win_addPeople.setFixedSize(self.win_addPeople.size())
        self.btn_settings.clicked.connect(self.open_settings)
        self.win_settings = WidgetSettings(self)
        self.win_athletesArr = WidgetAthletes(self)
        self.btn_athletesArr.clicked.connect(self.open_athletesArr)
        self.win_nominations = WidgetNominations(self)
        self.btn_category.clicked.connect(self.open_nominations)
        self.wins = [self, self.win_settings, self.win_addPeople, self.win_athletesArr, self.win_nominations]
        for i in self.wins:  # установление фиксированного размера окна, установка иконки приложения
            i.setFixedSize(i.size())
            i.setWindowIcon(QtGui.QIcon('img/icon.png'))


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

    def open_athletesArr(self):
        self.win_athletesArr.show()
        self.close()

    def open_nominations(self):
        self.win_nominations.show()
        self.close()


class WidgetAddPeople(QMainWindow, Ui_addPeople):
    def __init__(self, parent: Menu):
        self.parent = parent
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Добавить спортсмена')
        self.but_menu.clicked.connect(parent.show_menu)
        self.addButton.clicked.connect(self.press_button)

    def press_button(self):
        try:
            somebody = get_person(self)
            add_person(self.parent.db_con, somebody)
            self.parent.db_con.commit()
        except Exception:
            pass


class WidgetSettings(QMainWindow, Ui_settings):
    def __init__(self, parent: Menu):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.but_menu.clicked.connect(parent.show_menu)
        self.clear_database.clicked.connect(self.click_clear_database)
        self.save_database_txt.clicked.connect(self.click_save_txt)

    def click_clear_database(self):
        valid = QMessageBox.question(
            self, '', 'Действительно отчистить Базу данных?',
            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if valid == QMessageBox.StandardButton.Yes:
            clear_database(self.parent)

    def click_save_txt(self):
        arr = get_filterArr(self.parent.db_con)
        fname = QFileDialog.getSaveFileUrl(self)[0].toLocalFile()
        with open(fname, 'w', encoding='utf-8') as f:
            f.write('\n'.join(map(lambda x: ', '.join(map(str, x)), arr)))


class WidgetAthletes(QMainWindow, Ui_athletes):
    def __init__(self, parent: Menu):
        self.parent = parent
        super().__init__()
        self.setupUi(self)
        self.but_menu.clicked.connect(parent.show_menu)
        self.foundButton.clicked.connect(self.press_button)

    def press_button(self):
        weight = self.getWeight_Combo.currentText()
        year = self.getYear_lineEdit.text()
        league = self.getLeague_ComboBox.currentText()
        surname = self.getSurname_LineEdit.text()
        arr = get_filterArr(self.parent.db_con, weight=weight, year=year, league=league, surname=surname)
        change_tableWidget(self, arr)


class WidgetNominations(QMainWindow, Ui_nominations):
    def __init__(self, parent: Menu):
        self.parent = parent
        super().__init__()
        self.setupUi(self)
        self.but_menu.clicked.connect(parent.show_menu)
        self.dialog = WidgetNomination_dialog(self)
        self.create_button.clicked.connect(self.open_create_dialog)

    def open_create_dialog(self):  # Закрытие окна диалога вместе с родителем
        self.dialog.exec()

    def close(self):
        super().close()
        self.dialog.close()


class WidgetNomination_dialog(QDialog, Ui_nomination_dialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setFixedSize(self.size())
        self.setWindowIcon(QtGui.QIcon('img/icon.png'))
        self.create_button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        weight_class = self.getWeight_Combo.currentText()
        age = self.getAge_Combo.currentText()
        league = self.getLeague_ComboBox.currentText()
        nomination = self.getNomination_ComboBox.currentText()
        arr = get_filterArr(self.parent.parent.db_con,
                            league=league, age=age, nomination=nomination, weight_class=weight_class)
        change_tableWidget(self.parent, arr)


def change_tableWidget(self, arr):
    self.tableWidget.setRowCount(len(arr))
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            self.tableWidget.setItem(i, j, QTableWidgetItem(str(arr[i][j])))


def startGUI():
    enable_high_resolution()
    app = QApplication(sys.argv)
    win_main = Menu()
    win_main.show()
    sys.exit(app.exec())
