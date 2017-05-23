import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from .gui.mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


# Set of commands after saving the file in Qt Designer:
# python setup.py build_ui
# pip install -e .
# python -m myapp