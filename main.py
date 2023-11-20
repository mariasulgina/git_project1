import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = 50
        ellipse = QGraphicsEllipseItem(0, 0, diameter, diameter)
        ellipse.setPos(10, 10)
        ellipse.setBrush(QColor(255, 255, 0))  # желтый цвет
        self.scene.addItem(ellipse)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

