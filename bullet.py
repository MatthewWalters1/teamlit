'''
    this is the file for bullet objects
'''
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap
import random

class bullet(QGraphicsPixmapItem):
    def __init__(self, x_pos, y_pos, image_name, x_vel, y_vel):
        super().__init__()

        self.setPixmap(QPixmap(image_name))

        #spawns bullet at a random location at the top going in a random direction
        self.setX(x_pos)
        self.setY(y_pos)
        self.xVel = x_vel
        self.yVel = y_vel