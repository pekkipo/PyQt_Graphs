import sys
from PyQt5 import QtGui, QtCore, QtWidgets as qw

count = 1


class Main(qw.QMainWindow):
    def __init__(self):
        qw.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        centralwidget = qw.QWidget()
        self.add = qw.QPushButton("Add Node")
        self.grid = qw.QGridLayout()
        self.grid.addWidget(self.add, 0, 0)
        centralwidget.setLayout(self.grid)
        self.setCentralWidget(centralwidget)

        self.add.clicked.connect(self.Add)

        # ---------Window settings --------------------------------

        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle("")
        self.setWindowIcon(QtGui.QIcon(""))
        self.setStyleSheet("background-color:")
        self.show()


    def Add(self):
        global count

        b = qw.QPushButton(str(count), self)
        b.clicked.connect(self.Button)

        self.grid.addWidget(b, count, 0)

        count += 1


    def Button(self):
        sender = self.sender()
        print(sender.text())


def main():
    app = qw.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()