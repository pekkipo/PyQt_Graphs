from PyQt5.QtGui  import QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QApplication

class GameWindow(QGraphicsView):
    def __init__( self, parent = None ):
        super().__init__(parent)

        self.sx = 635
        self.sy = 475

        scene = QGraphicsScene(0,0,self.sx,self.sy)
        self.setScene(scene)

        self.x = 0
        self.y = 0
        self.w = 30
        self.h = 30
        pen   = QPen(QColor('dodgerblue'))
        #pen   = QPen(QColor(Qt.green))
        brush = QBrush(pen.color())
        #brush = QBrush(pen.color().darker(150))

        # As opposed to using QPen and QBrush, this colors the periphery only
        #dot = scene.addEllipse(self.x, self.y, self.w, self.h, QColor('dodgerblue'))

        self.dot = scene.addEllipse(self.x, self.y, self.w, self.h, pen, brush)
        self.dot.setFlag(QGraphicsItem.ItemIsMovable)


if  __name__ == '__main__':
    import sys

    fps = 50
    refresh_period = 1000/fps # ms

    app = QApplication(sys.argv)

    gw = GameWindow()
    gw.resize(640,480)
    gw.show()


    # if the steps match the gw aspect ratio, the dot will move along the main diagonal,
    # otherwise the dot will drift
    xstep = 4
    ystep = 3
    #ystep = xstep * gw.sy / gw.sx

    def moveDot():
       # In place of the next four lines, one can have a function
       # or a feed from an external source to update gw.x and gw.y
       gw.x += xstep
       gw.x %= gw.sx

       gw.y += ystep
       gw.y %= gw.sy

       gw.dot.setRect(gw.x,gw.y,gw.w,gw.h)

    timer = QTimer()
    timer.timeout.connect(moveDot)

    # Comment this line out to be able to click and drag the dot
    timer.start(refresh_period)

    sys.exit(app.exec_())