import sys, area, main, database
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import pygame

windowSizeOpenHeight = 720
windowSizeOpenWidth = 600
windowStartLocationX = 540
windowStartLocationY = 25

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Generic Space Game")
        self.setWindowIcon(QIcon(QPixmap("Images/fighter.png")))

        # Set window size and color
        self.setFixedSize(windowSizeOpenWidth, windowSizeOpenHeight)
        self.move(windowStartLocationX, windowStartLocationY)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(173, 216, 230))
        self.setPalette(palette)

        # Create central widget and the main layout
        centralwidget = QWidget()
        self.mainLayout = QVBoxLayout()

        # Align main layout
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add the background image
        self.gameoverImage = QPixmap("Images/main.png")
        self.gameoverPalette = QPalette()
        self.gameoverPalette.setBrush(QPalette.ColorRole.Window, QBrush(self.gameoverImage))
        self.setPalette(self.gameoverPalette)

        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(20)

        centralwidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralwidget)

        # Button that takes the player back to the main menu
        self.menuButton = QPushButton()
        self.menuButton.setText("Main Menu")
        self.menuButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.menuButton.clicked.connect(self.restartGame)

        # Button that takes the player back to the settings menu
        self.settingbutton = QPushButton()
        self.settingbutton.setText("Settings")
        self.settingbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.settingbutton.clicked.connect(self.settingClicked)
        
        # Button that displays the leaderboard
        self.boardbutton = QPushButton()
        self.boardbutton.setText("Leaderboard")
        self.boardbutton.setStyleSheet("background-color: lightGray;"
                                       "border-style: outset;"
                                       "border-width: 1px;"
                                       "border-color: black;"
                                       "min-width: 80 em;"
                                       "max-width: 80 em;"
                                       "padding: 6 px;")
        self.boardbutton.clicked.connect(self.boardClicked)

        # Button that exits the game
        self.exitButton = QPushButton()
        self.exitButton.setText("Exit")
        self.exitButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.exitButton.clicked.connect(self.exitClicked)

    
    def restartGame(self):
        QApplication.closeAllWindows()

        self.window = MainMenuWindow()
        self.window.show()
    
    def settingClicked(self):
        QApplication.closeAllWindows

        self.newWindow = SettingsWindow()
        self.newWindow.show()
    
    def boardClicked(self):
        # Sets boardText to a formatted string containing the top ten scores in a right-justified column and their winners on the left
        boardText = database.getTopScores()

        # Pops up a leaderboard (in the form of a message box) with the top ten scores and the players who won them
        leaderboard = QMessageBox(self)
        font = QFont("Consolas", 12, QFont.Weight.Bold)
        leaderboard.setFont(font)
        leaderboard.setStyleSheet("background-color: #293D48;"
                                  "color: white;"
                                  "min-width: 300 em;"
                                  "padding: 10 px;")
        leaderboard.setWindowTitle('Leaderboard')
        leaderboard.setWindowIcon(QIcon('Images/leaderboardicon.png'))
        leaderboard.setStandardButtons(QMessageBox.StandardButton.Ok)
        leaderboard.button(QMessageBox.StandardButton.Ok).setStyleSheet("background-color: lightGray;"
                                                                        "color: black;")
        leaderboard.setText(boardText)
        leaderboard.exec()

    def exitClicked(self):
        sys.exit()


class EndWindow(MenuWindow):
    def __init__(self, score):
        super().__init__()

        # Add the Game Over graphic
        self.titleLabel = QLabel()
        self.titleImage = QPixmap("Images/gameover.png")
        self.titleLabel.setPixmap(self.titleImage)
        self.mainLayout.addWidget(self.titleLabel)

        # Display the player's score
        self.scoreLabel = QLabel("Final Score:")
        self.scoreLabel.setStyleSheet(  "color: black;"
                                        "font-weight: bold;"
                                        "font-size: 20px;"
                                        "border: 5px solid white;"
                                        "padding: 3 px;")
        self.scoreLabel.setText("Final Score: " + str(score))
        self.scoreLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.scoreLabel)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)

        self.buttonLayout.addWidget(self.menuButton)
        self.buttonLayout.addWidget(self.settingbutton)
        self.buttonLayout.addWidget(self.boardbutton)
        self.buttonLayout.addWidget(self.exitButton)      

        self.mainLayout.addLayout(self.buttonLayout)

        # Prompts the user for a name and adds the score to the leaderboard, if desired
        nameEntered = False
        self.playerName, nameEntered = QInputDialog.getText(self, 'Name Dialog', 'Enter a name 1-16 characters long:\n (Leave empty if you do not wish to add your name and score)', QLineEdit.EchoMode.Normal, 'Name')
        if nameEntered and self.playerName:
            if len(self.playerName) <=16 and not self.playerName.isspace():
                database.addScore(self.playerName, score)
            else:
                while True:
                    self.playerName, nameEntered = QInputDialog.getText(self, 'Name Dialog', 'Invalid name. Try one that is 1-16 characters long:\n (Leave empty if you do not wish to add your name and score)', QLineEdit.EchoMode.Normal, 'Name')
                    if nameEntered and self.playerName:
                        if len(self.playerName) <=16 and not self.playerName.isspace():
                            database.addScore(self.playerName, score)
                            break
                    else:
                        break

class pvpEndWindow(MenuWindow):
    def __init__(self, winner):
        super().__init__()

        self.buttonLayout = QHBoxLayout()

        # Align button layout
        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)

        # Add the PvP win graphic
        self.titleLabel = QLabel()
        if winner == "Player 2":
            self.titleImage = QPixmap("Images/Player2.png")
        if winner == "Player 1":
            self.titleImage = QPixmap("Images/Player1.png")
        self.titleLabel.setPixmap(self.titleImage)
        self.mainLayout.addWidget(self.titleLabel)

        self.buttonLayout.addWidget(self.menuButton)
        self.buttonLayout.addWidget(self.settingbutton)
        self.buttonLayout.addWidget(self.exitButton)

        self.mainLayout.addLayout(self.buttonLayout)

class MainMenuWindow(MenuWindow):
    def __init__(self):
        super().__init__()

        self.window = area.Window()

        self.buttonLayout = QVBoxLayout()

        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Add title graphic
        self.titleLabel = QLabel()
        self.titleImage = QPixmap("Images/logo.png")
        self.titleLabel.setPixmap(self.titleImage)

        # Button that starts the game
        self.startButton = QPushButton()
        self.startButton.setText("Start Game")
        self.startButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 80 em;"
                                        "max-width: 80 em;"
                                        "padding: 6 px;")
        self.startButton.clicked.connect(self.startGame)
        self.buttonLayout.addWidget(self.startButton)

        # Button that takes the player to tutorial mode
        self.tutorialbutton = QPushButton()
        self.tutorialbutton.setText("Tutorial Mode")
        self.tutorialbutton.setStyleSheet("background-color: lightGray;"
                                       "border-style: outset;"
                                       "border-width: 1px;"
                                       "border-color: black;"
                                       "min-width: 80 em;"
                                       "max-width: 80 em;"
                                       "padding: 6 px;")
        self.tutorialbutton.clicked.connect(self.tutorialClicked)
        self.buttonLayout.addWidget(self.tutorialbutton)

        # Button that takes the player to PvP mode
        self.pvpbutton = QPushButton()
        self.pvpbutton.setText("PvP Mode")
        self.pvpbutton.setStyleSheet("background-color: lightGray;"
                                       "border-style: outset;"
                                       "border-width: 1px;"
                                       "border-color: black;"
                                       "min-width: 80 em;"
                                       "max-width: 80 em;"
                                       "padding: 6 px;")
        self.pvpbutton.clicked.connect(self.pvpClicked)
        self.buttonLayout.addWidget(self.pvpbutton)
        
        self.buttonLayout.addWidget(self.boardbutton)

        self.settingbutton.setStyleSheet("background-color: lightGray;"
                                       "border-style: outset;"
                                       "border-width: 1px;"
                                       "border-color: black;"
                                       "min-width: 80 em;"
                                       "max-width: 80 em;"
                                       "padding: 6 px;")
        self.buttonLayout.addWidget(self.settingbutton)

        self.exitButton.setStyleSheet("background-color: lightGray;"
                                       "border-style: outset;"
                                       "border-width: 1px;"
                                       "border-color: black;"
                                       "min-width: 80 em;"
                                       "max-width: 80 em;"
                                       "padding: 6 px;")
        self.buttonLayout.addWidget(self.exitButton)

        self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addLayout(self.buttonLayout)

    def pvpClicked(self):
        QApplication.closeAllWindows()

        self.form = main.Timer()
        self.view = QGraphicsView(self.window)

        self.view.setWindowTitle("Generic Space Game")
        self.view.setWindowIcon(QIcon(QPixmap("Images/fighter.png")))

        self.window.pauseButton.clicked.connect(self.form.pauseTimer)
        self.window.resumeButton.clicked.connect(self.form.startTimer)
        self.window.pvpInit()

        # Connects the update timer to the update functions of the background and objects of the window
        for i in self.window.enemyList:
            self.form.updateTimer.timeout.connect(i.update)
        for i in self.window.shotList:
            self.form.updateTimer.timeout.connect(i.update)

        self.form.updateTimer.timeout.connect(self.window.player.update)
        self.form.updateTimer.timeout.connect(self.window.updateBackground)
        self.form.movementTimer.timeout.connect(self.window.updatePvPMovement)

        self.view.setFixedSize(windowSizeOpenWidth, windowSizeOpenHeight)
        self.view.move(windowStartLocationX, windowStartLocationY)

        self.view.show()

    def tutorialClicked(self):
        QApplication.closeAllWindows()

        self.form = main.Timer()
        self.view = QGraphicsView(self.window)

        self.view.setWindowTitle("Generic Space Game")
        self.view.setWindowIcon(QIcon(QPixmap("Images/fighter.png")))

        self.window.pauseButton.clicked.connect(self.form.pauseTimer)
        self.window.resumeButton.clicked.connect(self.form.startTimer)
        self.window.tutorialInit()

        # Connects the update timer to the update functions of the background and objects of the window
        for i in self.window.enemyList:
            self.form.updateTimer.timeout.connect(i.update)
        for i in self.window.shotList:
            self.form.updateTimer.timeout.connect(i.update)

        self.form.updateTimer.timeout.connect(self.window.player.update)
        self.form.updateTimer.timeout.connect(self.window.updateBackground)
        self.form.movementTimer.timeout.connect(self.window.updateMovement)

        self.view.setFixedSize(windowSizeOpenWidth, windowSizeOpenHeight)
        self.view.move(windowStartLocationX, windowStartLocationY)

        self.view.show()

    def startGame(self):
        QApplication.closeAllWindows()

        self.window.isPaused = False

        self.form = main.Timer()
        self.view = QGraphicsView(self.window)
        
        self.view.setWindowTitle("Generic Space Game")
        self.view.setWindowIcon(QIcon(QPixmap("Images/fighter.png")))

        self.window.pauseButton.clicked.connect(self.form.pauseTimer)
        self.window.resumeButton.clicked.connect(self.form.startTimer)
        self.window.tutorial = False
        self.window.pvp = False

        # Connects the update timer to the update functions of the background and objects of the window
        for i in self.window.enemyList:
            self.form.updateTimer.timeout.connect(i.update)
        for i in self.window.shotList:
            self.form.updateTimer.timeout.connect(i.update)

        self.form.timer.timeout.connect(self.window.spawnEnemy)
        self.form.updateTimer.timeout.connect(self.window.player.update)
        self.form.updateTimer.timeout.connect(self.window.updateBackground)
        self.form.movementTimer.timeout.connect(self.window.updateMovement)

        self.view.setFixedSize(windowSizeOpenWidth, windowSizeOpenHeight)
        self.view.move(windowStartLocationX, windowStartLocationY)

        self.view.show()

class SettingsWindow(MenuWindow):
    def __init__(self):
        super().__init__()

        # Create the layouts
        self.buttonLayout = QVBoxLayout()
        self.volumeLayout = QHBoxLayout()

        # Align layouts
        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.volumeLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)

        self.titleLabel = QLabel()
        self.titleImage = QPixmap("Images/settings.png")
        self.titleLabel.setPixmap(self.titleImage)
        self.mainLayout.addWidget(self.titleLabel)

        # Button that mutes the music and sounds
        self.muteButton = QPushButton()
        if main.globalIsMuted == False:
            self.muteButton.setText("Mute")
        else:
            self.muteButton.setText("UnMute")

        self.muteButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 80 em;"
                                        "max-width: 80 em;"
                                        "padding: 6 px;")
        self.muteButton.clicked.connect(self.muteClicked)
        self.buttonLayout.addWidget(self.muteButton)

        # Button that sets the volume to low
        self.volumelow = QPushButton()
        self.volumelow.setText("Low")
        self.volumelow.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 80 em;"
                                        "max-width: 80 em;"
                                        "padding: 6 px;")
        self.volumelow.clicked.connect(self.setLow)
        self.volumeLayout.addWidget(self.volumelow)

        # Button that sets the volume to normal
        self.volumenormal = QPushButton()
        self.volumenormal.setText("Normal")
        self.volumenormal.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 80 em;"
                                        "max-width: 80 em;"
                                        "padding: 6 px;")
        self.volumenormal.clicked.connect(self.setNormal)
        self.volumeLayout.addWidget(self.volumenormal)

        # Button that sets the volume to high
        self.volumehigh = QPushButton()
        self.volumehigh.setText("High")
        self.volumehigh.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 80 em;"
                                        "max-width: 80 em;"
                                        "padding: 6 px;")
        self.volumehigh.clicked.connect(self.setHigh)
        self.volumeLayout.addWidget(self.volumehigh)

        self.buttonLayout.addLayout(self.volumeLayout)

        # Button that returns to the main menu
        self.returnButton = QPushButton()
        self.returnButton.setText("Return to Menu")
        self.returnButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 80 em;"
                                        "max-width: 80 em;"
                                        "padding: 6 px;")
        self.returnButton.clicked.connect(self.returnClicked)
        self.buttonLayout.addWidget(self.returnButton)

        self.mainLayout.addLayout(self.buttonLayout)

    def returnClicked(self):
        QApplication.closeAllWindows()

        self.window = MainMenuWindow()
        self.window.show()

    def setLow(self):
        pygame.mixer.music.set_volume(0.1)
        main.currentVolume = 0.1

    def setNormal(self):
        pygame.mixer.music.set_volume(0.4)
        main.currentVolume = 0.4

    def setHigh(self):
        pygame.mixer.music.set_volume(0.8)
        main.currentVolume = 0.8

    def muteClicked(self):
        if main.globalIsMuted == False:
            main.globalIsMuted = True
            main.StopMusic(pygame.mixer)
            self.muteButton.setText("UnMute")
        else:
            main.globalIsMuted = False
            main.StartMusic(pygame.mixer)
            self.muteButton.setText("Mute")