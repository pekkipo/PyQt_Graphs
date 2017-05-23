# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/alexeysergeevich/Desktop/PyQt_Graphs/myapp/gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gSettings = QtWidgets.QGroupBox(self.centralWidget)
        self.gSettings.setGeometry(QtCore.QRect(760, 20, 221, 221))
        self.gSettings.setStyleSheet("#gSettings {\n"
"background-color: rgba(170, 231, 195, 156);\n"
"}")
        self.gSettings.setObjectName("gSettings")
        self.addNode = QtWidgets.QPushButton(self.gSettings)
        self.addNode.setGeometry(QtCore.QRect(10, 30, 201, 61))
        self.addNode.setStyleSheet("#addNode {\n"
"background-color: rgba(226, 226, 226, 171);\n"
"    font: 16pt \"Avenir Next\";\n"
"\n"
"border: none;\n"
"\n"
"}")
        self.addNode.setObjectName("addNode")
        self.label = QtWidgets.QLabel(self.gSettings)
        self.label.setGeometry(QtCore.QRect(20, 40, 41, 41))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("circle_7609.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gView = QtWidgets.QGraphicsView(self.centralWidget)
        self.gView.setGeometry(QtCore.QRect(25, 20, 711, 641))
        self.gView.setStyleSheet("#gView {\n"
"\n"
"background-color: rgba(170, 231, 195, 156);\n"
"border: 2;\n"
"    border-color: rgb(90, 137, 155);\n"
"}")
        self.gView.setObjectName("gView")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(310, 80, 91, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("circle_7609.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(150, 280, 91, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("circle_7609.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hello, world!"))
        self.gSettings.setTitle(_translate("MainWindow", "Graph\'s settings"))
        self.addNode.setText(_translate("MainWindow", "       Add Node"))

