from PyQt5 import QtGui, QtCore, QtWidgets as qw

class Window(qw.QWidget):
    def __init__(self):
        qw.QWidget.__init__(self)
        self.view = View(self)
        self.button = qw.QPushButton('Clear View', self)
        self.button.clicked.connect(self.handleClearView)
        layout = qw.QVBoxLayout(self)
        layout.addWidget(self.view)
        layout.addWidget(self.button)

    def handleClearView(self):
        self.view.scene().clear()

class View(qw.QGraphicsView):
    def __init__(self, parent):
        qw.QGraphicsView.__init__(self, parent)
        self.setScene(qw.QGraphicsScene(self))
        self.setSceneRect(QtCore.QRectF(self.viewport().rect()))

    def mousePressEvent(self, event):
        self._start = event.pos()

    def mouseReleaseEvent(self, event):
        start = QtCore.QPointF(self.mapToScene(self._start))
        end = QtCore.QPointF(self.mapToScene(event.pos()))
        self.scene().addItem(
            qw.QGraphicsLineItem(QtCore.QLineF(start, end)))
        for point in (start, end):
            text = self.scene().addSimpleText(
                '(%d, %d)' % (point.x(), point.y()))
            text.setBrush(QtCore.Qt.red)
            text.setPos(point)

if __name__ == '__main__':

    import sys
    app = qw.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())