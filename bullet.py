'''
    this is the file for bullet objects
'''
from PyQt6.QtWidgets import QGraphicsScene, QApplication, QGraphicsView, QGraphicsItem, QGraphicsPixmapItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter
from player import *
#right now the bullet item looks just like the player object, but once I see how the play area works and how to add items to it, I will 
#work on this
class bullet(QGraphicsItem):
    def __init__(self):
        super.__init__(self)
        self.boundingRect(0, 0, 10, 10)
        self.shape = QPixmap()
        self.shape.load("beam1.png")

        #these will depend on how bullet generation works, so for now we won't do anything with them
        self.setX()
        self.setY()

    def bulletEvents(self):
        #collision with player
        collision = self.collidingItems()

        for item in collision:
            if isinstance(item, player):
                #need to finish score class
                #edit score 
                #edit health
