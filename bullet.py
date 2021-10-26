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

class ship(QGraphicsPixmapItem):
    def __init__(self, x_pos, y_pos, image_name, x_vel, y_vel, health):
        super().__init__()

        self.setPixmap(QPixmap(image_name))

        self.once = 1
        self.shipType = 'b'
        if image_name == "Images/enemy2.png":
            self.shipType = 'a'
        # else:
        #     self.shipType = 'b'
        self.health = health
        self.points = health * 20
        #spawns an enemy ship that will move at the speeds/directions given
        self.setX(x_pos)
        self.setY(y_pos)
        self.xVel = x_vel
        self.yVel = y_vel

        #this counts to a random number before shooting a bullet at the player
        self.shot = 0
        self.reload = random.randrange(4,20)