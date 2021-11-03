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

        self.setGeometry(windowStartLocationX, windowStartLocationY, windowSizeOpenWidth, windowSizeOpenHeight) #Set window size and color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(173, 216, 230))
        self.setPalette(palette)

        centralwidget = QWidget() #Create central widget and the main layouts
        self.buttonLayout = QHBoxLayout()
        self.mainLayout = QVBoxLayout()

        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)

        self.titleLabel = QLabel("Game Over!")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)

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

        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(20)

        self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addLayout(self.buttonLayout)

        self.setFixedSize(windowSizeOpenWidth, windowSizeOpenHeight)
        centralwidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralwidget)

        self.scene = QGraphicsScene(-50, -50, 600, 600)
        main.globalIsPaused = True

        nameEntered = False
        self.playerName, nameEntered = QInputDialog.getText(self, 'Name Dialog', 'Enter a name 1-16 characters long:\n (Leave empty if you do not wish to add your name and score)', QLineEdit.EchoMode.Normal, 'Name')
        if nameEntered and self.playerName and len(self.playerName) <=16 and not self.playerName.isspace():
            database.addScore(self.playerName, main.globalScore)
        else:
            while True:
                self.playerName, nameEntered = QInputDialog.getText(self, 'NameDialog', 'Invalid name. Try one that is 1-16 characters long:\n (Leave empty if you do not wish to add your name and score)', QLineEdit.EchoMode.Normal, 'Name')
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
        leaderboard = QMessageBox()
        leaderboard.setText(boardText)
        leaderboard.exec()

    def restartGame(self):
        QApplication.closeAllWindows()

        self.window = MainMenuWindow()
        self.window.show()

class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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

        self.titleLabel = QLabel("Main Menu")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignHCenter)

        self.startButton = QPushButton() #Button that starts the game
        self.startButton.setText("Start Game")
        self.startButton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 70 em;"
                                        "max-width: 70 em;"
                                        "padding: 6 px;")
        self.startButton.clicked.connect(self.startGame)
        self.buttonLayout.addWidget(self.startButton)

        self.settingbutton = QPushButton() #Button that takes the player back to the setting menu (currently does nothing)
        self.settingbutton.setText("Settings")
        self.settingbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 70 em;"
                                        "max-width: 70 em;"
                                        "padding: 6 px;")
        self.buttonLayout.addWidget(self.settingbutton)

        self.exitbutton = QPushButton() #Button that exits the game
        self.exitbutton.setText("Exit")
        self.exitbutton.setStyleSheet("background-color: lightGray;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 70 em;"
                                        "max-width: 70 em;"
                                        "padding: 6 px;")
        self.exitbutton.clicked.connect(self.exitClicked)
        self.buttonLayout.addWidget(self.exitbutton)

        self.boardbutton = QPushButton()
        self.boardbutton.setText("Leaderboard")
        self.boardbutton.setStyleSheet("background-color: lightGray;"
                                       "border-style: outset;"
                                       "border-width: 1px;"
                                       "border-color: black;"
                                       "min-width: 70 em;"
                                       "max-width: 70 em;"
                                       "padding: 6 px;")
        self.boardbutton.clicked.connect(self.boardClicked)
        self.buttonLayout.addWidget(self.boardbutton)

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
        leaderboard = QMessageBox()
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