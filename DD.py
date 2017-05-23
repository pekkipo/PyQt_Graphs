import sys
from PyQt5 import QtWidgets as qw, QtGui, QtCore


class combo(qw.QComboBox):
    def __init__(self, title, parent):
        super(combo, self).__init__(parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)

        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())


class Example(qw.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        lo = qw.QFormLayout()
        lo.addRow(qw.QLabel("Type some text in textbox and drag it into combo box"))

        edit = qw.QLineEdit()
        edit.setDragEnabled(True)
        com = combo("Button", self)
        lo.addRow(edit, com)
        self.setLayout(lo)
        self.setWindowTitle('Simple drag & drop')


def main():
    app = qw.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()