'''

    Project Name: Teamlit CS340 Project
    Authors: Jacob Page, Matthew Walters, Lillian Sharpe, and Victor Hanset
    This is the main for the project and contains the timer class and brings the play field, menus, and the player togther to form the game

'''
from PyQt6.QtWidgets import QGraphicsView, QWidget, QLabel, QApplication, QVBoxLayout
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QBrush, QColor, QFont
import sys
import area

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

    def showTime(self):
        self.time += 1
        self.displayTime.setText(str(self.time))

    def startTimer(self):
        self.timer.start(1000)

    def pauseTimer(self): #Pauses the timer
        self.timer.stop()

    def endGame(self): #This denotes the game has ended and all options will now be displayed
        self.pauseTimer()
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = area.Window()
    form = Timer()
    view = QGraphicsView(window)

    window.buttonLayout.addWidget(form)
    window.pauseButton.clicked.connect(form.pauseTimer)
    window.resumeButton.clicked.connect(form.startTimer)

    # Connects the update timer to the update functions of the background and objects of the window
    for i in window.enemyList:
        form.updateTimer.timeout.connect(i.update)
    form.updateTimer.timeout.connect(window.player.update)
    form.updateTimer.timeout.connect(window.updateBackground)

    view.show()
    form.show()

    sys.exit(app.exec())
