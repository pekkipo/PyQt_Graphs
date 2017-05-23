import sys, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets as qw

class Entry(qw.QLineEdit):
    def __init__(self,parent=None):
        qw.QLineEdit.__init__(self,parent)
        self.resize(75,50)
    def paintEvent(self,event):
        painter=QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawEllipse(54,25,20,20)
        painter.drawRect(QRect(0,0,self.width()-22,self.height()-1))
        font=QFont('Arial',13)
        painter.setFont(font)
        painter.drawText(QPoint(22,22),self.text())
        painter.end()
        #movements from https://stackoverflow.com/questions/12219727/dragging-moving-a-qpushbutton-in-pyqt
    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
        super(Entry, self).mousePressEvent(event)
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos
        super(Entry, self).mouseMoveEvent(event)
    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return
        super(Entry, self).mouseReleaseEvent(event)
class Add(qw.QWidget):
    def __init__(self,parent=None):
        qw.QWidget.__init__(self,parent)
        self.resize(75,50)
    def paintEvent(self, event):
        #use QPainter for a custom look
        painter=QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawEllipse(0,25,20,20)
        painter.drawEllipse(0,0,20,20)
        painter.drawRect(QRect(20,0,34,49))
        painter.drawEllipse(53,24,20,20)
        font=QFont('Arial',13)
        painter.setFont(font)
        painter.drawText(QPoint(22,22),"Add")
        painter.end()
    #movements from https://stackoverflow.com/questions/12219727/dragging-moving-a-qpushbutton-in-pyqt
    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
        super(Add, self).mousePressEvent(event)
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos
        super(Add, self).mouseMoveEvent(event)
    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return
        super(Add, self).mouseReleaseEvent(event)
class Window(qw.QMainWindow):
    def __init__(self):
        qw.QMainWindow.__init__(self)
        self.resize(640,480)
        self.add=Add(self)
        self.entry1=Entry(self)
        self.entry2=Entry(self)
if __name__=="__main__":
    app=qw.QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())