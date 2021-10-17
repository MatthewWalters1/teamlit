'''
    this is the file for all things related to the player object
'''
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap

class player(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

        self.health = 100
        
        #test different start positions for when it is added to the play area
        self.setX(100)
        self.setY(100)

        #this is the bounding rectangle of the player object in the graphics scene, and the image itself
        self.setPixmap(QPixmap("Images/fighter.png"))

class player_bullet(QGraphicsPixmapItem):
    def __init__(self, x, y):
        super().__init__()

        self.setPixmap(QPixmap("Images/beam2.png"))

        #spawns bullet at a random location at the top going in a random direction
        self.setX(x)
        self.setY(y)
        self.xVel = 0
        self.yVel = -20