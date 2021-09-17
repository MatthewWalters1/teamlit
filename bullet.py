'''
    this is the file for bullet objects
'''
from PyQt6.QtWidgets import QGraphicsScene, QApplication, QGraphicsView, QGraphicsItem 
#right now the bullet item looks just like the player object, but once I see how the play area works and how to add items to it, I will 
#work on this
class bullet(QGraphicsItem):
    def __init__(self):
        
        #
        super.__init__(self, t, obj)
        
        #these will depend on how bullet generation works, so for now we won't do anything with them
        self.setX()
        self.setY()