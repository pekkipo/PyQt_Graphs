import sys
from PyQt5 import QtWidgets as qw, QtGui
# QtGui in order to add images

#
# def window():
#     app = qw.QApplication(sys.argv)
#     w = qw.QWidget()
#     b = qw.QPushButton(w)
#     l1 = qw.QLabel(w)
#     l2 = qw.QLabel(w)
#     w.setWindowTitle('PyQt')
#     l1.setText("Text 1")
#     l2.setPixmap(QtGui.QPixmap('beatle.jpg'))
#     b.setText("Push me")
#
#     # Change size of the window
#     w.setGeometry(100, 100, 300, 200)  # 300 width 200 height
#
#     l1.move(130, 20)  # left down
#     l2.move(130, 50)
#
#     w.show()
#     sys.exit(app.exec_())

# Resizable box
def window():
    app = qw.QApplication(sys.argv)
    w = qw.QWidget()
    b = qw.QPushButton(w)
    l = qw.QLabel(w)
    v_box = qw.QVBoxLayout()

    w.setWindowTitle('PyQt')
    l.setText("Text 1")
    b.setText("Push me")

    #
    h_box = qw.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()  # label will be in the middle

    #
    v_box.addWidget(b)
    v_box.addLayout(h_box)

    w.setLayout(v_box)



    # Change size of the window
    w.setGeometry(100, 100, 300, 200)  # 300 width 200 height

    w.show()
    sys.exit(app.exec_())



window()


