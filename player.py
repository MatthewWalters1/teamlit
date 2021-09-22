'''
    this is the file for all things related to the player object
'''
from PyQt6.QtWidgets import QGraphicsScene, QApplication, QGraphicsView, QGraphicsItem 
from PyQt6.QtCore import Qt
class player(QGraphicsItem):
    def __init__(self):
        
        #not sure how exactly QGraphicsItems are initialized, so check on this
        super.__init__(self, t, obj)
        
        #test different start positions for when it is added to the play area
        self.setX(100)
        self.setY(100)
        self.xVel = 0
        self.yVel = 0
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            #change velocitiy
            xVel = -20
            
        elif event.key() == Qt.Key_Right:
            #change velocity
            xVel = 20

        elif event.key() == Qt.Key_Up:
            #change velocity
            yVel = -20 #may change depending on where 0, 0 is

        elif event.key() == Qt.Key_Down:
            #change velocity
            yVel = 20 #may change depending on where 0, 0 is