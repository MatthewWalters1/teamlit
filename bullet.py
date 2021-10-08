'''
    this is the file for bullet objects
'''
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
import random

class bullet(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

        self.setPixmap(QPixmap("Images/beam1.png"))

        #spawns bullet at a random location at the top going in a random direction
        self.setX(random.randrange(0, 600))
        self.setY(0)
        self.xVel = random.randrange(10, 30)
        self.yVel = random.randrange(20, 40)