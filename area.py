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
        
    # Resize can adjust to expanding the window but the window cannot be sized down
    def resizeEvent(self, event):
        self.canvas.pixmap = self.canvas.pixmap.scaled(self.width() - 22, self.height() - 22)
        self.canvas.setPixmap(self.canvas.pixmap)
        self.canvas.resize(self.width(), self.height())

class Canvas(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Initialize pixmap with a size and color
        self.pixmap = QPixmap(1000, 500)
        self.pixmap.fill(QColor("blue"))
        self.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
        
