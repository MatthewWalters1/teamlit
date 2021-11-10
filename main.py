'''

    Project Name: Teamlit CS340 Project
    Authors: Jacob Page, Matthew Walters, Lillian Sharpe, and Victor Hanset
    This is the main for the project and contains the timer class and brings the play field, menus, and the player togther to form the game

'''
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import QTimer
import sys, windowmanager
import pygame   

from playsound import playsound

globalIsPaused = False
globalIsMuted = False
globalScore = 0
globalTime = 0

currentVolume = 0.4

class Timer(QWidget): #Manages the game timer
    def __init__(self):
        super().__init__()

        self.timer = QTimer()
        self.endButtonPressed = False
        
        #self.timer.timeout.connect(self.showTime) #Initializes the timer to 0 and starts the timer
        self.time = 0
        self.startTimer()

        # Millisecond-interval update timer for constantly refreshing the background and objects
        self.updateTimer = QTimer()
        self.updateTimer.start(1)

        #Timer for movement
        self.movementTimer = QTimer()
        self.movementTimer.start(100)

    def startTimer(self):
        self.timer.start(1000)

    def pauseTimer(self): #Pauses the timer
        self.timer.stop()

def StopMusic(musicPlayer):
    musicPlayer.music.stop()

def StartMusic(musicPlayer):
    musicPlayer.music.load('Sounds/background.wav')
    musicPlayer.music.set_volume(currentVolume)
    musicPlayer.music.play(-1)

if __name__ == '__main__':

    pygame.mixer.init()
    StartMusic(pygame.mixer)

    app = QApplication(sys.argv)

    window = windowmanager.MainMenuWindow()
    window.show()

    sys.exit(app.exec())

