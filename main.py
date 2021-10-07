'''

    Project Name: Teamlit CS340 Project
    Authors: Jacob Page, Matthew Walters, Lillian Sharpe, and Victor Hanset
    This is the main for the project and contains the timer class and brings the play field, menus, and the player togther to form the game

'''
from PyQt6.QtWidgets import QGraphicsView, QWidget, QLabel, QApplication, QVBoxLayout
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QBrush, QColor, QFont
import sys, area

class Timer(QWidget): #Manages the game timer
    def __init__(self):
        super().__init__()

        self.displayTime = QLabel('0') #Creates the label that the time will be printed on
        self.displayTime.setFont(QFont("Times", 10, QFont.Weight.Medium))
        self.displayTime.setStyleSheet("background-color: white;"
                                        "color: black;"
                                        "min-width: 15 px;"
                                        "max-width: 15 px;"
                                        "min-height: 15 px;"
                                        "max-height: 15 px;")
        self.timer = QTimer()
        layout = QVBoxLayout()
        
        layout.setAlignment(Qt.AlignmentFlag.AlignBottom) #Layout to display the timer
        layout.addWidget(self.displayTime)
        self.setLayout(layout)

        self.timer.timeout.connect(self.showTime) #Intializes the timer to 0 and starts the timer
        self.timeLeft = 0
        self.startTimer()

    def showTime(self):
        time = self.timeLeft + 1
        self.timeLeft = self.timeLeft + 1
        self.displayTime.setText(str(time))

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
    window.setBackgroundBrush(QBrush(QColor(173, 216, 230)))

    view.show()
    form.show()

    sys.exit(app.exec())
