# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtGui, QtCore, QtWidgets as qw
from array import *

"""
Base class for a node. Contains all the inilization, drawing, and containing inputs and outputs
"""
class node(qw.QGraphicsRectItem):

    width = 100
    height = 100
    color = 1
    x = 90
    y = 60
    inputs=[]
    outputs=[]
    viewObj = None

    def __init__(self, n_x, n_y, n_width,n_height):
        qw.QGraphicsRectItem.__init__(self, n_x, n_y, n_width, n_height)
        self.width = n_width
        self.height = n_height
        self.x = n_x
        self.y = n_y
        self.setFlag(qw.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(qw.QGraphicsItem.ItemIsSelectable, True)
        self.iniNodeData()

    def mousePressEvent(self, e):
        print("Square got mouse press event")
        print("Event came to us accepted: %s"%(e.isAccepted(),))
        qw.QGraphicsRectItem.mousePressEvent(self, e)

    def mouseReleaseEvent(self, e):
        print("Square got mouse release event")
        print("Event came to us accepted: %s"%(e.isAccepted(),))
        qw.QGraphicsRectItem.mouseReleaseEvent(self, e)

    """
    This is where inputs and outputs will be created based on node type
    """
    def iniNodeData(self):
        print('making node data')
        for j in range(5):
            this = self
            x = input(this,0, 0+(j*10))
            self.inputs.append(x)

        for k in range(5):
            this = self
            x = output(this,self.x+self.width, self.y+(k*10))
            self.outputs.append(x)


    def mouseMoveEvent(self, event):
        print('Dragging@')
        qw.QGraphicsRectItem.mouseMoveEvent(self, event)


    def mousePressEvent(self, event):

        print('moving!')

"""
Nodes will evaluate from the last node to the first node, therefore inputs are evaluted
"""
class input(qw.QGraphicsRectItem):
    currentConnectedNode = None
    currentConnectedOutput = None
    parentNode = None
    width = 10
    height = 10
    x = 1
    y = 1
    color = 1
    drawItem = None

    def __init__(self, pnode, posX, posY):
        self.parentNode = pnode
        self.x = posX
        self.y = posY
        self.color = 1
        qw.QGraphicsRectItem.__init__(self, self.x+self.parentNode.x, self.y+self.parentNode.y, self.width, self.height, self.parentNode)



'''
Output value from a node
'''
class output(node):
    parentNode = None
    width = 10
    height = 10
    x = 1
    y = 1

    def __init__(self, pnode, posX, posY):
        self.parentNode = pnode
        self.x = posX
        self.y = posY
        self.color = 1
        qw.QGraphicsRectItem.__init__(self, self.x-self.width, self.y, self.width, self.height, self.parentNode)


'''
Check Click events on the scene Object
'''
class Scene(qw.QGraphicsScene):


    nodes = []

    def mousePressEvent(self, e):
        print("Scene got mouse press event")
        print("Event came to us accepted: %s"%(e.isAccepted(),))
        qw.QGraphicsScene.mousePressEvent(self, e)

    def mouseReleaseEvent(self, e):
        print("Scene got mouse release event")
        print("Event came to us accepted: %s"%(e.isAccepted(),))
        qw.QGraphicsScene.mouseReleaseEvent(self, e)

    def dragMoveEvent(self, e):
        print('Scene got drag move event')

    def addNode(self):
        newNode = self.addItem(node(250,250,100,150))
        self.nodes.append(newNode)


'''
Main Window Object
'''

class MainWindowUi(qw.QMainWindow):
    def __init__(self):
        qw.QMainWindow.__init__(self)
        self.setWindowTitle('RIS RIB Generator')
        self.scene = Scene(0, 0, 800, 850, self)
        self.view = qw.QGraphicsView()
        self.setCentralWidget(self.view)
        self.view.setScene(self.scene)


        exitAction = qw.QAction(QtGui.QIcon('beatle.jpg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        newNodeAction = qw.QAction(QtGui.QIcon('beatle.jpg'), 'New Node', self)
        newNodeAction.setStatusTip('Add a blank node')
        newNodeAction.triggered.connect(self.scene.addNode)


        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newNodeAction)
        fileMenu.addAction(exitAction)


'''
Start Point
'''

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    win = MainWindowUi()
    win.show()
    sys.exit(app.exec_())