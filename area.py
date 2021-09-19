'''
    area.py
    teamlit
    Creates an application window with a canvas
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        centralWidget = QWidget()

        centralLayout = QVBoxLayout()
        centralLayout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        centralWidget.setLayout(centralLayout)

        self.canvas = Canvas()
        centralLayout.addWidget(self.canvas)

        self.setCentralWidget(centralWidget)
        

class Canvas(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # QPixmap is currently set to a fixed size
        pixmap = QPixmap(1000, 500)
        pixmap.fill(QColor("blue"))
        self.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
        
