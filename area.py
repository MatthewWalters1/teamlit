'''
    area.py
    teamlit
    Creates an application window with a canvas
'''

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsScene, QGraphicsItem
import player

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        centralWidget = QWidget()

        centralLayout = QVBoxLayout()

        # PyQt5: centralLayout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        centralWidget.setLayout(centralLayout)


        self.buttonLayout = QHBoxLayout()

        self.pauseButton = QPushButton()
        self.pauseButton.setText("Pause")
        self.buttonLayout.addWidget(self.pauseButton)
        
        self.exitButton = QPushButton()
        self.exitButton.setText("Exit")
        self.exitButton.clicked.connect(self.exitClicked)
        self.buttonLayout.addWidget(self.exitButton)

        centralLayout.addLayout(self.buttonLayout)


        self.canvas = Canvas()
        centralLayout.addWidget(self.canvas)

        self.setCentralWidget(centralWidget)

        #here will be the scene for all the moving objects
        self.scene = QGraphicsScene(-50, -50, 600, 600)

    # Resize can adjust to expanding the window but the window cannot be sized down
    def resizeEvent(self, event):
        self.canvas.resize(self.width(), self.height())


    def exitClicked(self, event):
        sys.exit(app)


class Canvas(QLabel):
    def __init__(self):
        super().__init__()

        #PyQt5: self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Initialize pixmap with a size and color
        self.pixmap = QPixmap(1000, 500)
        self.pixmap.fill(QColor("blue"))
        self.setPixmap(self.pixmap)


    def resizeEvent(self, event):
        self.pixmap = self.pixmap.scaled(self.width(), self.height())
        self.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
        
