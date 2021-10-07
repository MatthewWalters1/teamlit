'''
    this is the file for bullet objects
'''
from PyQt6.QtWidgets import QGraphicsScene, QApplication, QGraphicsView, QGraphicsItem, QGraphicsPixmapItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter
import random

#right now the bullet item looks just like the player object, but once I see how the play area works and how to add items to it, I will 
#work on this
class bullet(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()
        #self.boundingRect(0, 0, 10, 10)
        #self.shape = QPixmap()
        #self.shape.load("beam1.png")
        self.setPixmap(QPixmap("Images/beam1.png"))

        #these will depend on how bullet generation works, so for now we won't do anything with them
        self.setX(random.randrange(0, 600))
        self.setY(0)
        self.xVel = random.randrange(10, 30)
        self.yVel = random.randrange(20, 40)