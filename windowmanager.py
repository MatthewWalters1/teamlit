import sys, area, main, database
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

windowSizeOpenHeight = 1055
windowSizeOpenWidth = 600
windowStartLocationX = 540
windowStartLocationY = 25

class EndWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generic Space Game")
        self.setWindowIcon(QIcon(QPixmap("Images/fighter.png")))
        self.setGeometry(windowStartLocationX, windowStartLocationY, windowSizeOpenWidth, windowSizeOpenHeight) #Set window size and color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(173, 216, 230))
        self.setPalette(palette)

        centralwidget = QWidget() #Create central widget and the main layouts
        self.buttonLayout = QHBoxLayout()
        self.mainLayout = QVBoxLayout()

        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignCenter)

        self.titleLabel = QLabel()
        self.titleImage = QPixmap("Images/gameover.png")
        self.titleLabel.setPixmap(self.titleImage)
        self.mainLayout.addWidget(self.titleLabel)

        self.gameoverImage = QPixmap("Images/main.png")
        self.gameoverPalette = QPalette()
        self.gameoverPalette.setBrush(QPalette.ColorRole.Window, QBrush(self.gameoverImage))
        self.setPalette(self.gameoverPalette)

        self.scoreLabel = QLabel("Final Score:")
        self.scoreLabel.setStyleSheet(  "color: black;"
                                        "font-weight: bold;"
                                        "font-size: 20px;"
                                        "border: 5px solid white;"
                                        "padding: 3 px;")

        self.scoreLabel.setText("Final Score: " + str(main.globalScore))
        self.scoreLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.scoreLabel)

        self.menuButton = QPushButton() #Button that takes the player back to the main menu
        self.menuButton.setText("Main Menu")
        self.menuButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.menuButton.clicked.connect(self.restartGame)
        self.buttonLayout.addWidget(self.menuButton)

        self.settingbutton = QPushButton() #Button that takes the player back to the setting menu (currently does nothing)
        self.settingbutton.setText("Settings")
        self.settingbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.buttonLayout.addWidget(self.settingbutton)

        self.boardbutton = QPushButton() # Button that displays the leaderboard
        self.boardbutton.setText("Leaderboard")
        self.boardbutton.setStyleSheet("background-color: lightGray;"
                                       "border-style: outset;"
                                       "border-width: 1px;"
                                       "border-color: black;"
                                       "min-width: 80 em;"
                                       "max-width: 80 em;"
                                       "padding: 6 px;")
        self.boardbutton.clicked.connect(self.boardClicked)
        self.buttonLayout.addWidget(self.boardbutton)

        self.exitbutton = QPushButton() #Button that exits the game
        self.exitbutton.setText("Exit")
        self.exitbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 60 em;"
                                        "max-width: 60 em;"
                                        "padding: 6 px;")
        self.exitbutton.clicked.connect(self.exitClicked)
        self.buttonLayout.addWidget(self.exitbutton)

        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(20)

        self.mainLayout.addLayout(self.buttonLayout)

        self.setFixedSize(windowSizeOpenWidth, windowSizeOpenHeight)
        centralwidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralwidget)

        self.scene = QGraphicsScene(-50, -50, 600, 600)
        main.globalIsPaused = True

        # Prompts the user for a name and adds the score to the leaderboard, if desired
        nameEntered = False
        self.playerName, nameEntered = QInputDialog.getText(self, 'Name Dialog', 'Enter a name 1-16 characters long:\n (Leave empty if you do not wish to add your name and score)', QLineEdit.EchoMode.Normal, 'Name')
        if nameEntered and self.playerName:
            if len(self.playerName) <=16 and not self.playerName.isspace():
                database.addScore(self.playerName, main.globalScore)
            else:
                while True:
                    self.playerName, nameEntered = QInputDialog.getText(self, 'Name Dialog', 'Invalid name. Try one that is 1-16 characters long:\n (Leave empty if you do not wish to add your name and score)', QLineEdit.EchoMode.Normal, 'Name')
                    if nameEntered and self.playerName:
                        if len(self.playerName) <=16 and not self.playerName.isspace():
                            database.addScore(self.playerName, main.globalScore)
                            break
                    else:
                        break

    def exitClicked(self):
        sys.exit()

    def boardClicked(self):
        boardText = database.getTopScores()
        leaderboard = QMessageBox(self)
        font = QFont("Consolas", 12)
        leaderboard.setFont(font)
        leaderboard.setStyleSheet("background-color: darkGreen;"
                                  "min-width: 300 em;"
                                  "padding: 10 px;")
        leaderboard.setWindowTitle('Leaderboard')
        leaderboard.setWindowIcon(QIcon('Images/leaderboardicon.png'))
        leaderboard.setStandardButtons(QMessageBox.StandardButton.Ok)
        leaderboard.button(QMessageBox.StandardButton.Ok).setStyleSheet("background-color: green")
        leaderboard.setText(boardText)
        leaderboard.exec()

    def restartGame(self):
        QApplication.closeAllWindows()

        self.window = MainMenuWindow()
        self.window.show()

class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generic Space Game")
        self.setWindowIcon(QIcon(QPixmap("Images/fighter.png")))
        self.window = area.Window()
        self.setGeometry(windowStartLocationX, windowStartLocationY, windowSizeOpenWidth, windowSizeOpenHeight) #Set window size and color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(173, 216, 230))
        self.setPalette(palette)

        centralwidget = QWidget() #Create central widget and the main layouts
        self.buttonLayout = QVBoxLayout()
        self.mainLayout = QVBoxLayout()

        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)

        #self.titleLabel = QLabel("Main Menu")
        #self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)
        self.titleLabel = QLabel()
        self.titleImage = QPixmap("Images/logo.png")
        self.titleLabel.setPixmap(self.titleImage)

        self.backgroundImage = QPixmap("Images/main.png")
        self.backgroundPalette = QPalette()
        self.backgroundPalette.setBrush(QPalette.ColorRole.Window, QBrush(self.backgroundImage))
        self.setPalette(self.backgroundPalette)

        self.startButton = QPushButton() #Button that starts the game
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
        self.buttonLayout.addWidget(self.boardbutton)

        self.settingbutton = QPushButton() #Button that takes the player back to the setting menu (currently does nothing)
        self.settingbutton.setText("Settings")
        self.settingbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 80 em;"
                                        "max-width: 80 em;"
                                        "padding: 6 px;")
        self.buttonLayout.addWidget(self.settingbutton)

        self.exitbutton = QPushButton() #Button that exits the game
        self.exitbutton.setText("Exit")
        self.exitbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 80 em;"
                                        "max-width: 80 em;"
                                        "padding: 6 px;")
        self.exitbutton.clicked.connect(self.exitClicked)
        self.buttonLayout.addWidget(self.exitbutton)

        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(20)

        self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addLayout(self.buttonLayout)

        self.setFixedSize(windowSizeOpenWidth, windowSizeOpenHeight)
        centralwidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralwidget)

        self.scene = QGraphicsScene(-50, -50, 600, 600)

    def exitClicked(self, event):
        sys.exit()

    def boardClicked(self):
        boardText = database.getTopScores()
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

    def startGame(self):
        QApplication.closeAllWindows()
        
        main.globalIsPaused = False

        self.form = main.Timer()
        self.view = QGraphicsView(self.window)

        self.window.buttonLayout.addWidget(self.form)
        self.window.pauseButton.clicked.connect(self.form.pauseTimer)
        self.window.resumeButton.clicked.connect(self.form.startTimer)

        # Connects the update timer to the update functions of the background and objects of the window
        for i in self.window.enemyList:
            self.form.updateTimer.timeout.connect(i.update)
        for i in self.window.shotList:
            self.form.updateTimer.timeout.connect(i.update)

        self.form.timer.timeout.connect(self.window.spawnEnemy)
        self.form.updateTimer.timeout.connect(self.window.player.update)
        self.form.updateTimer.timeout.connect(self.window.updateBackground)
        self.form.movementTimer.timeout.connect(self.window.updateMovement)

        self.view.setGeometry(windowStartLocationX, windowStartLocationY, windowSizeOpenWidth, windowSizeOpenHeight)
        self.view.setFixedSize(windowSizeOpenWidth, windowSizeOpenHeight)

        self.view.show()
        self.form.show()

class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generic Space Game")
        self.setWindowIcon(QIcon(QPixmap("Images/fighter.png")))
        self.setGeometry(windowStartLocationX, windowStartLocationY, windowSizeOpenWidth, windowSizeOpenHeight) #Set window size and color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(173, 216, 230))
        self.setPalette(palette)

        centralwidget = QWidget() #Create central widget and the main layouts
        self.buttonLayout = QVBoxLayout()
        self.mainLayout = QVBoxLayout()

        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)

        self.titleLabel = QLabel()
        self.titleImage = QPixmap("Images/settings.png")
        self.titleLabel.setPixmap(self.titleImage)
        self.mainLayout.addWidget(self.titleLabel)

        self.backgroundImage = QPixmap("Images/main.png")
        self.backgroundPalette = QPalette()
        self.backgroundPalette.setBrush(QPalette.ColorRole.Window, QBrush(self.backgroundImage))
        self.setPalette(self.backgroundPalette)

        self.muteButton = QPushButton() #Button that starts the game
        if main.globalIsMute == False:
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

        self.boardbutton = QPushButton()
        self.boardbutton.setText("Leaderboard")
        self.boardbutton.setStyleSheet("background-color: lightGray;"
                                       "border-style: outset;"
                                       "border-width: 1px;"
                                       "border-color: black;"
                                       "min-width: 80 em;"
                                       "max-width: 80 em;"
                                       "padding: 6 px;")
        self.buttonLayout.addWidget(self.boardbutton)

        self.settingbutton = QPushButton() #Button that takes the player back to the setting menu (currently does nothing)
        self.settingbutton.setText("Settings")
        self.settingbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 80 em;"
                                        "max-width: 80 em;"
                                        "padding: 6 px;")
        self.buttonLayout.addWidget(self.settingbutton)

        self.exitbutton = QPushButton() #Button that exits the game
        self.exitbutton.setText("Return to Menu")
        self.exitbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 80 em;"
                                        "max-width: 80 em;"
                                        "padding: 6 px;")
        self.exitbutton.clicked.connect(self.exitClicked)
        self.buttonLayout.addWidget(self.exitbutton)

        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(20)

        self.mainLayout.addLayout(self.buttonLayout)

        self.setFixedSize(windowSizeOpenWidth, windowSizeOpenHeight)
        centralwidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralwidget)

        self.scene = QGraphicsScene(-50, -50, 600, 600)

    def exitClicked(self, event):
        QApplication.closeAllWindows()

        self.window = MainMenuWindow()
        self.window.show()

    def muteClicked(self):
        if main.globalIsMute == False:
            main.globalIsMute = True
            self.muteButton.setText("UnMute")
        else:
            main.globalIsMute = False
            self.muteButton.setText("Mute")