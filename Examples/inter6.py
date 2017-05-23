#!/usr/bin/env python
# coding: utf-8

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets as qw

rad = 5

class Node(qw.QGraphicsEllipseItem):
    def __init__(self, path, index):
        super(Node, self).__init__(-rad, -rad, 2*rad, 2*rad)

        self.rad = rad
        self.path = path
        self.index = index

        self.setZValue(1)
        self.setFlag(qw.QGraphicsItem.ItemIsMovable)
        self.setFlag(qw.QGraphicsItem.ItemSendsGeometryChanges)
        self.setBrush(Qt.green)

    def itemChange(self, change, value):
        if change == qw.QGraphicsItem.ItemPositionChange:
            self.path.updateElement(self.index, value.toPoint())
        return qw.QGraphicsEllipseItem.itemChange(self, change, value)


class Path(qw.QGraphicsPathItem):
    def __init__(self, path, scene):
        super(Path, self).__init__(path)
        for i in range(path.elementCount()):
            node = Node(self, i)
            node.setPos(QPointF(path.elementAt(i)))
            scene.addItem(node)
        self.setPen(QPen(Qt.red, 1.75))

    def updateElement(self, index, pos):
        path.setElementPositionAt(index, pos.x(), pos.y())
        self.setPath(path)


if __name__ == "__main__":

    app = qw.QApplication([])

    path = QPainterPath()
    path.moveTo(0,0)
    path.cubicTo(-30, 70, 35, 115, 100, 100)
    path.lineTo(200, 100)
    path.cubicTo(200, 30, 150, -35, 60, -30)

    scene = qw.QGraphicsScene()
    scene.addItem(Path(path, scene))

    view = qw.QGraphicsView(scene)
    view.setRenderHint(QPainter.Antialiasing)
    view.resize(600, 400)
    view.show()
    app.exec_()