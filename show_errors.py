import sys
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

def show_errors():
    sys.excepthook = except_hook
