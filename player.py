'''
    this is the file for all things related to the player object
'''
from PyQt6.QtWidgets import QGraphicsScene, QApplication, QGraphicsView, QGraphicsItem 
class player(QGraphicsItem):
    def __init__(self):
        #not sure how exactly QGraphicsItems are initialized, so check on this
        super().__init__()
        #test different start positions for when it is added to the play area
        self.setX(100)
        self.setY(100)