import sys


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def show_errors():
    sys.excepthook = except_hook


from PyQt6 import QtCore, QtWidgets


def enable_high_resolution():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
