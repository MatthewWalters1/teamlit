import sys
import area
from PyQt6.QtWidgets import QGraphicsView, QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt6.QtCore import QTimer,QDateTime
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsScene, QGraphicsItem, QMessageBox

class Timer(QWidget): #Manages the game timer
    def __init__(self):
        super().__init__()

        self.displayTime=QLabel('0') #Creates the label that the time will be printed on

        layout=QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.timer=QTimer()

        self.timer.timeout.connect(self.showTime)
        self.timeLeft = 0

        layout.addWidget(self.displayTime)
        self.setLayout(layout)

        self.startTimer()

    def showTime(self):
        time = self.timeLeft + 1
        self.timeLeft = self.timeLeft + 1
        self.displayTime.setText(str(time))

    def startTimer(self):
        self.timer.start(1000)


    def endTimer(self):
        self.timer.stop()


if __name__ == '__main__':
    app=QApplication(sys.argv)

    window = area.Window()
    
    form=Timer()
    window.buttonLayout.addWidget(form)

    window.pauseButton.clicked.connect(form.endTimer)
    window.resumeButton.clicked.connect(form.startTimer)

    #window.setBackgroundBrush(QBrush(QColor(200, 0, 0)))

    form.show()
    view = QGraphicsView(window)

    #view.setBackgroundBrush(QBrush(QColor(200, 0, 0)))

    view.show()

    sys.exit(app.exec())