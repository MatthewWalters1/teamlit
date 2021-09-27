'''
    area.py
    teamlit
    Creates a resizable application window with two buttons
'''

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsScene, QGraphicsItem
import player

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Specify the dimensions and background color of the window
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: blue")
        

        # Create a widget with a button layout at the top right of the window
        centralWidget = QWidget()

        self.buttonLayout = QHBoxLayout()

        # PyQt5: buttonLayout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)


        # Add a pause button to the button layout
        self.pauseButton = QPushButton()
        self.pauseButton.setText("Pause")
        self.pauseButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 40 em;"
                                        "max-width: 40 em;"
                                        "padding: 6 px;")
                                        
        self.buttonLayout.addWidget(self.pauseButton)
        
        # Add an exit button to the button layout
        self.exitButton = QPushButton()
        self.exitButton.setText("Exit")
        self.exitButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 40 em;"
                                        "max-width: 40 em;"
                                        "padding: 6 px;")
        self.exitButton.clicked.connect(self.exitClicked)
        self.buttonLayout.addWidget(self.exitButton)

        # Add the button layout to the widget and set the widget as the central widget
        centralWidget.setLayout(self.buttonLayout)
        self.setCentralWidget(centralWidget)

        #here will be the scene for all the moving objects
        self.scene = QGraphicsScene(-50, -50, 600, 600)
        
    def exitClicked(self, event):
        sys.exit(app)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
        
