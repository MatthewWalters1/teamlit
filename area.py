'''
    area.py
    teamlit
    Creates a play window with two buttons (Pause and Exit), a player object, enemy bullets, and player bullets.
    The pause menu for the pause button is also implemented and includes four buttons (Resume, Main Menu, Restart, and Exit).
'''

from math import isqrt
import sys, random
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QPalette, QFont, QBrush
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsScene, QMessageBox, QApplication
import player
import bullet
import windowmanager
import main

class Window(QGraphicsScene):
    def __init__(self):
        super().__init__(-50, -50, 600, 600)

        self.isPaused = False

        # Create a widget with a button layout at the top right of the window
        centralWidget = QWidget()

        self.centralLayout = QVBoxLayout()
        self.centralLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.buttonLayout = QHBoxLayout()

        self.buttonLayout.setAlignment(Qt.AlignmentFlag.AlignRight)


        # Add a pause button to the button layout
        self.pauseButton = QPushButton()
        self.pauseButton.setText("Pause")
        self.pauseButton.setFont(QFont("Times", 10, QFont.Weight.Medium))
        self.pauseButton.setStyleSheet("background-color: lightGray;"
                                        "color: black;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 40 em;"
                                        "min-height: 15 em;"
                                        "max-height: 15 em;"
                                        "max-width: 40 em;"
                                        "padding: 6 px;")
        self.pauseButton.clicked.connect(self.pauseClicked)                                
        self.buttonLayout.addWidget(self.pauseButton)
        
        # Add an exit button to the button layout
        self.exitButton = QPushButton()
        self.exitButton.setText("Exit")
        self.exitButton.setFont(QFont("Times", 10, QFont.Weight.Medium))
        self.exitButton.setStyleSheet("background-color: lightGray;"
                                        "color: black;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 40 em;"
                                        "max-width: 40 em;"
                                        "min-height: 15 em;"
                                        "max-height: 15 em;"
                                        "padding: 6 px;")
        self.exitButton.clicked.connect(self.exitClicked)
        self.buttonLayout.addWidget(self.exitButton)

        self.resumeButton = QPushButton()
        self.resumeButton.setText("Resume")
        self.resumeButton.setFont(QFont("Times", 10, QFont.Weight.Medium))
        self.resumeButton.setStyleSheet("background-color: lightGray;"
                                        "color: black;"
                                        "border-style: outset;"
                                        "border-width: 1px;"
                                        "border-color: black;"
                                        "min-width: 55 em;"
                                        "max-width: 55 em;"
                                        "min-height: 15 em;"
                                        "max-height: 15 em;"
                                        "padding: 6 px;")

        # Add the button layout to the widget and set the widget as the central widget
        self.centralLayout.addLayout(self.buttonLayout)
        centralWidget.setLayout(self.centralLayout)

        #Sets the size and then the color of a widget and in this case it is what we call the central widget
        centralWidget.setFixedSize(600, 50)

        centralWidget.setGeometry(-50, -270, 600, 100)

        centralWidgetPallette = centralWidget.palette()
        centralWidgetPallette.setColor(QPalette.ColorRole.Window , QColor(194, 197, 204))
        centralWidget.setPalette(centralWidgetPallette)

        self.addWidget(centralWidget)

        #Add player to the screen
        self.player = player.player()
        self.player.setPos(self.width()/2-68, self.height()-100)
        self.addItem(self.player)
        
        #this is a list of bullets that the player shoots, it is added to on 'fireBullet'
        self.shotList = []
        self.enemyList = []
        
    def pauseClicked(self, event):
        if not self.isPaused:
            # Creates a message box to hold buttons to click when the game is paused
            self.pauseMenu = QMessageBox()
            self.pauseMenu.setText("Paused")
            self.pauseMenu.setFont(QFont("Times", 14, QFont.Weight.Medium))
            self.pauseMenu.setStyleSheet("background-color: white;"
                                         "color: black;"
                                         "padding: 6px;")
            
            # Adds the resume button to the pause menu
            self.pauseMenu.addButton(self.resumeButton, QMessageBox.ButtonRole.DestructiveRole)
            self.resumeButton.clicked.connect(self.resumeClicked)
            self.pauseMenu.setEscapeButton(self.resumeButton)

            # Adds a main menu button to the pause menu
            self.menuButton = QPushButton()
            self.menuButton.setText("Main Menu")
            self.menuButton.setFont(QFont("Times", 10, QFont.Weight.Medium))
            self.menuButton.setStyleSheet("background-color: lightGray;"
                                          "color: black;"
                                          "border-style: outset;"
                                          "border-width: 1px;"
                                          "border-color: black;"
                                          "min-width: 70 em;"
                                          "max-width: 70 em;"
                                          "min-height: 15 em;"
                                          "max-height: 15 em;"
                                          "padding: 6 px;")
            self.menuButton.clicked.connect(self.menuClicked)
            self.pauseMenu.addButton(self.menuButton, QMessageBox.ButtonRole.DestructiveRole)

            # Adds a restart button to the pause menu
            self.restartButton = QPushButton()
            self.restartButton.setText("Restart")
            self.restartButton.setFont(QFont("Times", 10, QFont.Weight.Medium))
            self.restartButton.setStyleSheet("background-color: lightGray;"
                                             "color: black;"
                                             "border-style: outset;"
                                             "border-width: 1px;"
                                             "border-color: black;"
                                             "min-width: 50 em;"
                                             "max-width: 50 em;"
                                             "min-height: 15 em;"
                                             "max-height: 15 em;"
                                             "padding: 6 px;")
            self.restartButton.clicked.connect(self.restartClicked)
            self.pauseMenu.addButton(self.restartButton, QMessageBox.ButtonRole.DestructiveRole)

            # Adds an exit button to pauseMenu
            self.pauseExitButton = QPushButton()
            self.pauseExitButton.setText("Exit")
            self.pauseExitButton.setFont(QFont("Times", 10, QFont.Weight.Medium))
            self.pauseExitButton.setStyleSheet("background-color: lightGray;"
                                            "color: black;"
                                            "border-style: outset;"
                                            "border-width: 1px;"
                                            "border-color: black;"
                                            "min-width: 45 em;"
                                            "max-width: 45 em;"
                                            "min-height: 15 em;"
                                            "max-height: 15 em;"
                                            "padding: 6 px;")
            self.pauseExitButton.clicked.connect(self.exitClicked)
            self.pauseMenu.addButton(self.pauseExitButton, QMessageBox.ButtonRole.DestructiveRole)


            self.addWidget(self.pauseMenu)

            main.globalIsPaused = True
                
            self.pauseMenu.open()

            # Moves pauseMenu to the center of the scene
            centerX = int(self.sceneRect().center().x())
            centerY = int(self.sceneRect().center().y())
            self.pauseMenu.move(centerX - self.pauseMenu.width()/2, centerY - self.pauseMenu.width()/2)
    
    def resumeClicked(self, event):
        self.isPaused = False

    def restartClicked(self, event):
        QApplication.closeAllWindows()

        self.newWindow = windowmanager.MainMenuWindow()
        self.newWindow.startGame()

    def menuClicked(self, event):
        QApplication.closeAllWindows()

        self.newWindow = windowmanager.MainMenuWindow()
        self.newWindow.show()

    def exitClicked(self, event):
        sys.exit()

    def spawnEnemy(self):
        self.enemy = bullet.bullet(random.randrange(0, 600), 0, "Images/beam1.png", random.randrange(10, 15), random.randrange(15, 20))
        self.addItem(self.enemy)
        self.enemyList.append(self.enemy)

    #here, use x and y to determine the position the bullet will start at
    def fireBullet(self, x, y):
        self.shot = bullet.bullet(x + 3, y, "Images/beam2.png", 0, -30)
        self.addItem(self.shot)
        self.shotList.append(self.shot)
        self.shot = bullet.bullet(x + 39, y, "Images/beam2.png", 0, -30)
        self.addItem(self.shot)
        self.shotList.append(self.shot)
        
    def keyPressEvent(self, event):
        if not self.isPaused:
            xVel = 0
            yVel = 0
            if event.key() == Qt.Key.Key_Left:
                #change velocitiy
                xVel = -40 #may change if too fast/slow
                
            if event.key() == Qt.Key.Key_Right:
                #change velocity
                xVel = 40 #may change if too fast/slow

            if event.key() == Qt.Key.Key_Up:
                #change velocity
                yVel = -40 #may change if too fast/slow

            if event.key() == Qt.Key.Key_Down:
                #change velocity
                yVel = 40 #may change if too fast/slow

            if event.key() == Qt.Key.Key_Space:
                #fire bullet
                self.fireBullet(self.player.x(), self.player.y())

            self.player.setPos(self.player.x()+xVel, self.player.y()+yVel)


            if self.player.x() > self.width()-118:
                self.player.setPos(self.width()-118, self.player.y())

            if self.player.x() < -50:
                self.player.setPos(-50, self.player.y())

            if self.player.y() > self.height()-30:
                self.player.setPos(self.player.x(), self.height()-30)

            if self.player.y() < 0:
                self.player.setPos(self.player.x(), 0)

    def updateMovement(self):

        self.isPaused = main.globalIsPaused

        if not self.isPaused:  
            for item in self.enemyList:
                item.setPos(item.x()+item.xVel, item.y()+item.yVel)
                collision = item.collidingItems()
                for bang in collision:
                    if isinstance(bang, type(self.player)):
                        self.player.health -= random.randrange(15, 25)
                        self.enemyList.remove(item)
                        self.removeItem(item)
                        print("hit")
                        if self.player.health <= 0:
                            QApplication.closeAllWindows()
                            
                            main.globalIsPaused = True
                            self.windowmanager = windowmanager.EndWindow()
                            self.windowmanager.show()

                if item.x() > self.width()-70:
                    item.xVel = -item.xVel
                    item.setPos(self.width()-70, item.y())

                if item.x() < -60:
                    item.xVel = -item.xVel
                    item.setPos(-60, item.y())

                if item.y() > self.height()+10:
                    item.yVel = -item.yVel
                    item.setPos(item.x(), self.height()+10)

                if item.y() < -10:
                    item.yVel = -item.yVel
                    item.setPos(item.x(), -10)
             
            for item in self.shotList:
                item.setPos(item.x()+item.xVel, item.y()+item.yVel)
                if item.y() < -118:
                    self.shotList.remove(item)
                    self.removeItem(item)

    def updateBackground(self):
        self.setBackgroundBrush(QBrush(QColor(173, 216, 230)))
