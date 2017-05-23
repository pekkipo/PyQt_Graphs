import sys
from PyQt5 import QtGui, QtCore, QtWidgets as qw

class PicNode(qw.QTableWidget):
    def __init__(self):
        super(PicNode, self).__init__()
        picWidth = 960
        picHeight = 540

        self.setFixedSize(picWidth,picHeight+105)
        self.setRowCount(2)
        self.setColumnCount(1)
        self.setColumnWidth(0, picWidth)
        self.setRowHeight(0,picHeight)
        self.setRowHeight(1, 100)
        self.horizontalHeader().hide()
        self.verticalHeader().hide()

        img = QtGui.QPixmap("MV17_Pix BoxR.jpg")
        pic = qw.QLabel()
        pic.setPixmap(img.scaled(picWidth,picHeight))
        self.setCellWidget(0,0,pic)
        self.setItem(0,1,qw.QTableWidgetItem("some caption data goes here"))

class NodeGraph(qw.QGraphicsView):
    def __init__(self, parent):
        super(NodeGraph, self).__init__(parent)
        self._zoom = 0
        self._scene = qw.QGraphicsScene(self)
        self.CreatePicNode()
        self.CreatePicNode()
        self.CreatePicNode()

        self.setScene(self._scene)
        self.setTransformationAnchor(qw.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(qw.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
        self.setFrameShape(qw.QFrame.NoFrame)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setDragMode(qw.QGraphicsView.RubberBandDrag)

    def CreatePicNode(self):
        # create my node
        nodeProxy = qw.QGraphicsProxyWidget()
        nodeProxy.setWidget(PicNode())
        nodeProxy.setFlag(qw.QGraphicsItem.ItemStacksBehindParent, True)
        self._scene.addItem(nodeProxy)
        # create parent grabby item, sized a bit bigger than nodeProxy
        item1 = qw.QGraphicsRectItem(-5, -5, nodeProxy.rect().width() + 10, nodeProxy.rect().height() + 10)
        item1.setFlag(qw.QGraphicsItem.ItemIsMovable, True)
        item1.setFlag(qw.QGraphicsItem.ItemIsSelectable, True)
        self._scene.addItem(item1)
        # set parent
        nodeProxy.setParentItem(item1)

    def zoomFactor(self):
        return self._zoom

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.scale(1.1,1.1)
        else:
            self.scale(0.9, 0.9)

    def keyPressEvent(self, event):
        super(NodeGraph, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Space:
            self.setDragMode(qw.QGraphicsView.ScrollHandDrag)

    def mousePressEvent(self, event):
        super(NodeGraph, self).mousePressEvent(event)
        if event.buttons() == QtCore.Qt.MidButton:
            self.setDragMode(qw.QGraphicsView.ScrollHandDrag)

    def mouseDragEvent(self, event):
        super(NodeGraph, self).mouseDragEvent(event)

    def mouseReleaseEvent(self, event):
        super(NodeGraph, self).mouseReleaseEvent(event)
        self.setDragMode(qw.QGraphicsView.RubberBandDrag)

    def keyReleaseEvent(self, event):
        self.setDragMode(qw.QGraphicsView.RubberBandDrag)


class NodeGraphApp(qw.QDialog):
    def __init__(self):
        super(NodeGraphApp, self).__init__()
        self.initUI()

    def initUI(self):
        self.viewer = NodeGraph(self)
        layout = qw.QVBoxLayout(self)
        layout.addWidget(self.viewer)

        self.setWindowTitle("Nodegraph test")

def main():
    app = qw.QApplication(sys.argv)
    ex = NodeGraphApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()