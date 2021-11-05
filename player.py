'''
    this is the file for all things related to the player object
'''
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap

class player(QGraphicsPixmapItem):
    def __init__(self):
        super().__init__()

        # this is used to limit the player's ammo
        self.ammo = 30
        self.reload = 30
        
        self.health = 100
        self.setPixmap(QPixmap("Images/fighter.png"))