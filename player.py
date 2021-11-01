'''
    this is the file for all things related to the player object
'''
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap

class player(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

        self.health = 100
        self.setPixmap(QPixmap("Images/fighter.png"))