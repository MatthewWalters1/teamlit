'''
    this is the file for all things related to the player object
'''
from PyQt6.QtWidgets import QGraphicsScene, QApplication, QGraphicsView, QGraphicsItem, QGraphicsPixmapItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter

class player(QGraphicsItem):
    def __init__(self):
        #not sure how exactly QGraphicsItems are initialized, so check on this
        super.__init__(self)
        
        #test different start positions for when it is added to the play area
        self.setX(100)
        self.setY(100)
        self.xVel = 0
        self.yVel = 0
        #this is the bounding rectangle of the player object in the graphics scene, and the image itself
        self.boundingRect(0, 0, 30, 30)
        self.ship = QPixmap()
        self.ship.load("fighter.png")
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            #change velocitiy
            xVel = -20 #may change if too fast/slow
            
        elif event.key() == Qt.Key_Right:
            #change velocity
            xVel = 20 #may change if too fast/slow

        elif event.key() == Qt.Key_Up:
            #change velocity
            yVel = -20 #may change if too fast/slow

        elif event.key() == Qt.Key_Down:
            #change velocity
            yVel = 20 #may change if too fast/slow


##idea## score class
class score(QGraphicsItem):
    def __init__(self):
        super.__init__(self)
    
        self.score = 0
