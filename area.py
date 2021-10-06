'''
    area.py
    teamlit
    Creates a resizable application window with two buttons
'''

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsScene, QGraphicsItem, QMessageBox
import player
import timer

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Specify the dimensions and background color of the window
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: blue")
        

        # Create a widget with a button layout at the top right of the window
        centralWidget = QWidget()

        self.centralLayout = QVBoxLayout()
        self.centralLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.buttonLayout = QHBoxLayout()

        # PyQt5: buttonLayout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignRight)


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
        self.pauseButton.clicked.connect(self.pauseClicked)                                
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
        self.centralLayout.addLayout(self.buttonLayout)
        centralWidget.setLayout(self.centralLayout)
        self.setCentralWidget(centralWidget)

        #here will be the scene for all the moving objects
        self.scene = QGraphicsScene(-50, -50, 600, 600)

        #self.gametime = timer.GameTimer(600)
        
    def pauseClicked(self, event):
        #if not self.gametime.isPaused:
        self.pauseMenu = QMessageBox()
        self.pauseMenu.setText("Paused")
        self.resumeButton = QPushButton()
        self.resumeButton.setText("Resume")
        self.resumeButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 45 em;"
                                        "max-width: 45 em;"
                                        "padding: 6 px;")
        self.pauseMenu.addButton(self.resumeButton, QMessageBox.ButtonRole.DestructiveRole)
        #self.resumeButton.clicked.connect(self.gametime.toggle_pause)
        self.pauseExitButton = QPushButton()
        self.pauseExitButton.setText("Exit")
        self.pauseExitButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 45 em;"
                                        "max-width: 45 em;"
                                        "padding: 6 px;")
        self.pauseExitButton.clicked.connect(self.exitClicked)
        self.pauseMenu.addButton(self.pauseExitButton, QMessageBox.ButtonRole.DestructiveRole)
        self.pauseMenu.setEscapeButton(self.resumeButton)
        self.pauseMenu.setStyleSheet("background-color: white;"
                                    "padding: 6px;")
            
        self.menuLayout = QVBoxLayout()
        self.menuLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.menuLayout.addWidget(self.pauseMenu)
        self.centralLayout.addLayout(self.menuLayout)

        #self.gametime.toggle_pause()
            
        self.pauseMenu.open()

    def exitClicked(self, event):
        sys.exit(app)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()


    #self.gametime.start_timer()

        
