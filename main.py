'''

    Project Name: Teamlit CS340 Project
    Authors: Jacob Page, Matthew Walters, Lillian Sharpe, and Victor Hanset
    This is the main for the project and contains the timer class and brings the play field, menus, and the player togther to form the game

'''
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
import sys, windowmanager

globalIsPaused = False
globalScore = 0

class Timer(QWidget): #Manages the game timer
    def __init__(self):
        super().__init__()

        self.displayTime = QLabel('0') #Creates the label that the time will be printed on
        self.displayTime.setFont(QFont("Times", 10, QFont.Weight.Medium))
        self.displayTime.setStyleSheet("background-color: white;"
                                        "color: black;"
                                        "min-width: 40 px;"
                                        "max-width: 40 px;"
                                        "min-height: 15 px;"
                                        "max-height: 15 px;"
                                        "padding: 3 px;")
        self.displayTime.setTextFormat(Qt.TextFormat.PlainText)
        self.timer = QTimer()
        self.endButtonPressed = False
        layout = QVBoxLayout()
        
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter) #Layout to display the timer
        layout.addWidget(self.displayTime)
        self.setLayout(layout)

        self.timer.timeout.connect(self.showTime) #Initializes the timer to 0 and starts the timer
        self.time = 0
        self.startTimer()

        # Millisecond-interval update timer for constantly refreshing the background and objects
        self.updateTimer = QTimer()
        self.updateTimer.start(1)

        #Timer for movement
        self.movementTimer = QTimer()
        self.movementTimer.start(100)

    def showTime(self):
        self.time += 1
        self.displayTime.setText(str(self.time))

    def startTimer(self):
        self.timer.start(1000)

    def pauseTimer(self): #Pauses the timer
        self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = windowmanager.MainMenuWindow()
    window.show()

    sys.exit(app.exec())
    