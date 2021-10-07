'''
    area.py
    teamlit
    Creates a resizable application window with two buttons
'''

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsScene, QGraphicsItem, QMessageBox
import player
import bullet

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
                                        "min-width: 50 em;"
                                        "max-width: 50 em;"
                                        "min-height: 15 em;"
                                        "max-height: 15 em;"
                                        "padding: 6 px;")

        # Add the button layout to the widget and set the widget as the central widget
        self.centralLayout.addLayout(self.buttonLayout)
        centralWidget.setLayout(self.centralLayout)

        #Sets the size and then the color of a widget and in this case it is what we call the central widget
        centralWidget.setFixedSize(600, 50)

        centralWidget.setGeometry(-50, -50, 600, 100)

        centralWidgetPallette = centralWidget.palette()
        centralWidgetPallette.setColor(QPalette.ColorRole.Window , QColor(194, 197, 204))
        centralWidget.setPalette(centralWidgetPallette)

        self.addWidget(centralWidget)

        #Add player to the screen
        self.player = player.player()
        self.player.setPos(self.width()/2-68, self.height()/2-68)
        self.addItem(self.player)

        #Add enemies to the screen
        self.enemyList = []
        for i in range(5):
            self.enemy = bullet.bullet()
            self.addItem(self.enemy)
            self.enemyList.append(self.enemy)
        
    def pauseClicked(self, event):
        if not self.isPaused:
            self.pauseMenu = QMessageBox()
            self.pauseMenu.setText("Paused")
            self.pauseMenu.setFont(QFont("Times", 14, QFont.Weight.Medium))
            self.pauseMenu.setStyleSheet("background-color: white;"
                                        "color: black;")
            
            self.pauseMenu.addButton(self.resumeButton, QMessageBox.ButtonRole.DestructiveRole)
            self.resumeButton.clicked.connect(self.resumeClicked)

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
            self.pauseMenu.setEscapeButton(self.resumeButton)
            self.pauseMenu.setStyleSheet("background-color: white;"
                                        "color: black;"
                                        "padding: 6px;")

            # Adds pauseMenu to the center of the scene
            centerX = int(self.sceneRect().center().x())
            centerY = int(self.sceneRect().center().y())
            self.pauseMenu.setGeometry(centerX - 50, centerY - 50, 100, 100)
            self.addWidget(self.pauseMenu)

            self.isPaused = True
                
            self.pauseMenu.open()
    
    def resumeClicked(self, event):
        self.isPaused = False

    def exitClicked(self, event):
        sys.exit()

    def keyPressEvent(self, event):
        if not self.isPaused:
            xVel = 0
            yVel = 0
            if event.key() == Qt.Key.Key_Left:
                #change velocitiy
                xVel = -40 #may change if too fast/slow
                
            elif event.key() == Qt.Key.Key_Right:
                #change velocity
                xVel = 40 #may change if too fast/slow

            elif event.key() == Qt.Key.Key_Up:
                #change velocity
                yVel = -40 #may change if too fast/slow

            elif event.key() == Qt.Key.Key_Down:
                #change velocity
                yVel = 40 #may change if too fast/slow

            self.player.setPos(self.player.x()+xVel, self.player.y()+yVel)

            if self.player.x() > self.width()-118:
                self.player.setPos(self.width()-118, self.player.y())
            if self.player.x() < -50:
                self.player.setPos(-50, self.player.y())
            if self.player.y() > self.height()-118:
                self.player.setPos(self.player.x(), self.height()-118)
            if self.player.y() < 0:
                self.player.setPos(self.player.x(), 0)
            
            for item in self.enemyList:
                item.setPos(item.x()+item.xVel, item.y()+item.yVel)

                collision = item.collidingItems()
                for bang in collision:
                    if isinstance(bang, type(self.player)):
                        self.player.health -= 20
                        self.enemyList.remove(item)
                        self.removeItem(item)
                        print("hit")
                        if self.player.health <= 0:
                            print("Game Over!")
                            sys.exit()

                if item.x() > self.width()-80:
                    item.setPos(item.x()-80, item.y())
                    item.xVel = -item.xVel
                if item.x() < -50:
                    item.setPos(-50, item.y())
                    item.xVel = -item.xVel
                if item.y() > self.height()-87:
                    item.setPos(item.x(), self.height()-87)
                    item.yVel = -item.yVel
                if item.y() < 0:
                    item.setPos(item.x(), 0)
                    item.yVel = -item.yVel
            
'''
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
'''
