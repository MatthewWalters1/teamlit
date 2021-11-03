'''
    area.py
    teamlit
    Creates a play window with two buttons (Pause and Exit), a player object, enemy bullets, and player bullets.
    The pause menu for the pause button is also implemented and includes four buttons (Resume, Main Menu, Restart, and Exit).
'''

from math import isqrt
import sys, random
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette, QFont, QBrush, QPixmap
from PyQt6.QtWidgets import QGraphicsPixmapItem, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsScene, QMessageBox, QApplication
import player, bullet, windowmanager, main

class Window(QGraphicsScene):
    def __init__(self):
        super().__init__(-50, -50, 600, 600)

        self.imageOneStartX = -250
        self.imageOneStartY = -1000
        self.imageTwoStartX = -250
        self.imageTwoStartY = -2919

        self.imageMove = 0

        #this is your score, it gets added to when the player kills an enemy ship
        main.globalScore = 0
        # intensity controls the number of enemy ships on screen at once, it goes up over time
        self.intensity = 3
        # elapsed is how you measure when to increase intensity
        self.elapsed = 0
        # boss is used to measure how long between appearances bosses should spawn
        self.boss = 400

        main.globalIsPaused = True

        # Create a widget with a button layout at the top right of the window
        topWidget = QWidget()

        self.topLayout = QVBoxLayout()
        self.topLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

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

        # Add the button layout to the widget and set the widget as the top widget
        self.topLayout.addLayout(self.buttonLayout)
        topWidget.setLayout(self.topLayout)

        #Sets the size and then the color of a widget and in this case it is what we call the top widget
        topWidget.setFixedSize(600, 50)

        topWidget.setGeometry(-50, -270, 600, 100)

        topWidgetPallette = topWidget.palette()
        topWidgetPallette.setColor(QPalette.ColorRole.Window , QColor(194, 197, 204))
        topWidget.setPalette(topWidgetPallette)

        self.image = QGraphicsPixmapItem()
        self.image.setPixmap(QPixmap("Images/milkyway.png"))
        self.addItem(self.image)

        self.imageTwo = QGraphicsPixmapItem()
        self.imageTwo.setPixmap(QPixmap("Images/milkyway.png"))
        self.addItem(self.imageTwo)

        self.addWidget(topWidget)

        self.key_list = set()

        #Add player to the screen
        self.player = player.player()
        self.player.setPos(self.width()/2-68, self.height()-100)
        self.addItem(self.player)
        
        #this is a list of bullets that the player shoots, it is added to on 'fireBullet'
        self.shotList = []
        #this is a list of enemy ships that will be along the top of the screen
        self.enemyList = []
        #this is a list of bullets that the enemies shoot at the player
        self.projectileList = []
        
    def pauseClicked(self, event):
        if not main.globalIsPaused:
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
        main.globalIsPaused = False

    def restartClicked(self, event):
        self.newWindow = windowmanager.MainMenuWindow()
        self.newWindow.startGame()

        self.deleteSelf()

    def menuClicked(self, event):
        QApplication.closeAllWindows()

        self.newWindow = windowmanager.MainMenuWindow()
        self.newWindow.show()

        self.deleteSelf()

    def exitClicked(self, event):
        sys.exit()

    def spawnEnemy(self):
        if (len(self.enemyList) < self.intensity):
            self.enemyType = random.randrange(0,11)
            self.check = True
            for i in self.enemyList:
                if i.shipType == 'c' or i.shipType == 'd':
                    self.check = False
            if self.enemyType <= 4:
                self.enemy = bullet.ship(random.randrange(0, 480), -300, 'b', 0, 20, 1)
            elif self.enemyType <= 9:
                self.enemy = bullet.ship(random.randrange(0, 480), -300, 'a', 0, 10, 3)
            elif self.enemyType == 10 and self.check == True and self.boss > 400:
                self.boss = 0
                self.enemyType = random.randrange(0,2)
                if self.enemyType == 0:
                    self.enemy = bullet.ship(180, -400, 'c', 0, 10, 50)
                if self.enemyType == 1:
                    self.enemy = bullet.ship(180, -400, 'd', 0, 10, 80)
            else:
                self.enemy = bullet.ship(random.randrange(0, 480), -300, 'b', 0, 40, 1)
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
        if not main.globalIsPaused:
            self.key_list.add(event.key())

    def keyReleaseEvent(self, event):
        if not main.globalIsPaused:
            self.key_list.remove(event.key())

    def updateMovement(self):
        if not main.globalIsPaused:

            # this is used to stop bosses from appearing constantly
            self.boss += 1

            xVel = 0
            yVel = 0
            if Qt.Key.Key_Left in self.key_list:
                #change velocitiy
                xVel = -40 #may change if too fast/slow
                
            if Qt.Key.Key_Right in self.key_list:
                #change velocity
                xVel = 40 #may change if too fast/slow

            if Qt.Key.Key_Up in self.key_list:
                #change velocity
                yVel = -40 #may change if too fast/slow

            if Qt.Key.Key_Down in self.key_list:
                #change velocity
                yVel = 40 #may change if too fast/slow

            if Qt.Key.Key_Space in self.key_list:
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
            
            self.imageMove += 2

            self.image.setPos(self.imageOneStartX, (self.imageOneStartY + self.imageMove))
            self.imageTwo.setPos(self.imageTwoStartX, (self.imageTwoStartY + self.imageMove))

            if (self.imageOneStartY + self.imageMove) >= 1080:
                self.imageOneStartY = -2749 - self.imageMove

            if (self.imageTwoStartY + self.imageMove) >= 1080:
                self.imageTwoStartY = -2749 - self.imageMove

            self.elapsed += 1
            if self.elapsed == 200:
                self.elapsed = 0
                self.intensity += 1
            
            main.globalScore += 1 
            
            for item in self.enemyList:
                if item.shipType == 'b':
                    if item.y() >= 0:
                        item.yVel = 0
                        if item.once == 1:
                            item.xVel = random.randrange(-10, 10)
                            item.once = 0
                if item.shipType == 'c':
                    if item.y() <= -300:
                        item.yVel = self.intensity
                        if item.yVel > 10 or item.reload < 6:
                            item.yVel = 10
                            item.reload -= 1
                if item.shipType == 'd':
                    if item.y() >= -80:
                        item.yVel = 0
                        if item.once == 1:
                            item.xVel = 0
                            while (item.xVel == 0):
                                item.xVel = random.randrange(-4, 4)
                            item.once = 0
                item.shot += 1
                if item.shot > item.reload:
                        item.shot = 0

                item.setPos(item.x()+item.xVel, item.y()+item.yVel)
                collision = item.collidingItems()
                for bang in collision:
                    if isinstance(bang, type(self.player)):
                        self.player.health -= item.points
                        self.enemyList.remove(item)
                        self.removeItem(item)
                        print("hit")
                        if self.player.health <= 0:
                            QApplication.closeAllWindows()
                            
                            main.globalIsPaused = True
                            self.windowmanager = windowmanager.EndWindow()
                            self.windowmanager.show()

                            self.deleteSelf()

                if item.x() > self.width()-70:
                    item.xVel = -item.xVel
                    item.setPos(self.width()-70, item.y())

                if item.x() < -60:
                    item.xVel = -item.xVel
                    item.setPos(-60, item.y())

                if item.y() > self.height()+10:
                    self.enemyList.remove(item)
                    self.removeItem(item)

                if item.y() < -400:
                    item.yVel = -item.yVel
                    item.setPos(item.x(), -10)

                if item.shot >= item.reload:
                    if item.shipType == 'b':
                        self.p = bullet.bullet(item.x() + 16, item.y(), "Images/beam3.png", 0, 30)
                        self.addItem(self.p)
                        self.projectileList.append(self.p)
                    elif item.shipType == 'c':
                        self.p = bullet.bullet(item.x() + 50, item.y() + 50, "Images/beam3.png", 0, 30)
                        if self.player.x() > item.x() + 80:
                            self.p.xVel += 5
                        elif self.player.x() < item.x() - 10:
                            self.p.xVel -= 5
                        item.reload = 10
                        self.addItem(self.p)
                        self.projectileList.append(self.p)
                    elif item.shipType == 'd':
                        item.reload = 18
                        self.p = bullet.bullet(item.x() + 28, item.y() + 69, "Images/beam4a.png", 0, 20)
                        self.addItem(self.p)
                        self.projectileList.append(self.p)
             
            for item in self.shotList:
                item.setPos(item.x()+item.xVel, item.y()+item.yVel)
                # -300 is the current limit, this could change
                if item.y() < -300:
                    self.shotList.remove(item)
                    self.removeItem(item)
                    continue
                collision = item.collidingItems()
                for bang in collision:
                    # this is easier than isinstance, and it works
                    if bang in self.enemyList:
                        # this makes it to where the player has to be a little more intentional to kill the target
                        # In my tests, a lot of stray bullets would hit ships before they were even a threat
                        if bang.y() > -50 or bang.shipType == 'c' or bang.shipType == 'd':
                            bang.health -= 1
                        self.shotList.remove(item)
                        self.removeItem(item)
                        if bang.health == 0:
                            main.globalScore += bang.points
                            self.enemyList.remove(bang)
                            if bang.shipType == 'c' or bang.shipType == 'd':
                                # after the boss dies, we reset the timer so the player has about a minute without a boss on screen
                                self.boss = 0
                            self.removeItem(bang)
                            # you have to break, in case it collided with multiple enemies, since it will try to remove the bullet twice
                        break

            for item in self.projectileList:
                if item.image_name == "Images/beam4a.png":
                    if self.player.x() < item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4b", -5, 20)
                    elif self.player.x() > item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4e", 5, 20)
                    self.projectileList.remove(item)
                    self.removeItem(item)
                    self.projectileList.append(self.j)
                    self.addItem(self.j)
                elif item.image_name == "Images/beam4b.png":
                    if self.player.x() < item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4c", -10, 20)
                    elif self.player.x() > item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4a", 0, 20)
                    self.projectileList.remove(item)
                    self.removeItem(item)
                    self.projectileList.append(self.j)
                    self.addItem(self.j)
                elif item.image_name == "Images/beam4e.png":
                    if self.player.x() < item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4a", 0, 20)
                    elif self.player.x() > item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4f", 10, 20)
                    self.projectileList.remove(item)
                    self.removeItem(item)
                    self.projectileList.append(self.j)
                    self.addItem(self.j)
                elif item.image_name == "Images/beam4c.png":
                    if self.player.x() < item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4d", -15, 20)
                    elif self.player.x() > item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4b", -5, 20)
                    self.projectileList.remove(item)
                    self.removeItem(item)
                    self.projectileList.append(self.j)
                    self.addItem(self.j)
                elif item.image_name == "Images/beam4f.png":
                    if self.player.x() < item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4g", 15, 20)
                    elif self.player.x() > item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4e", 5, 20)
                    self.projectileList.remove(item)
                    self.removeItem(item)
                    self.projectileList.append(self.j)
                    self.addItem(self.j)
                elif item.image_name == "Images/beam4d.png":
                    if self.player.x() < item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4c", -10, 20)
                        self.projectileList.remove(item)
                        self.removeItem(item)
                        self.projectileList.append(self.j)
                        self.addItem(self.j)
                elif item.image_name == "Images/beam4g.png":
                    if self.player.x() > item.x():
                        self.j = bullet.bullet(item.x(), item.y(), "Images/beam4f", 10, 20)
                        self.projectileList.remove(item)
                        self.removeItem(item)
                        self.projectileList.append(self.j)
                        self.addItem(self.j)
                item.setPos(item.x() + item.xVel, item.y() + item.yVel)
                if item.y() > self.height() + 10:
                    self.projectileList.remove(item)
                    self.removeItem(item)
                collision = item.collidingItems()
                for bang in collision:
                    if isinstance(bang, type(self.player)):
                        self.player.health -= 15
                        self.projectileList.remove(item)
                        self.removeItem(item)
                        print("hit")
                        if self.player.health <= 0:
                            QApplication.closeAllWindows()
                            
                            main.globalIsPaused = True
                            self.windowmanager = windowmanager.EndWindow()
                            self.windowmanager.show()

                            self.deleteSelf()

    def updateBackground(self):
        self.setBackgroundBrush(QBrush(QColor(173, 216, 230)))

    def deleteSelf(self):
        main.globalIsPaused = True # Attempts to fix invisible bullet death problem
        print(str(main.globalScore))
        for i in self.views():
            i.close()
        for i in self.items():
            self.removeItem(i)
        self.clear()
        main.globalIsPaused = False
        self.deleteLater()

