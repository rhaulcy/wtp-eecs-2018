# Name :
# Collaborators :

# This file helps you start making tetris pieces, or tetronimoes.

from graphics import *

class Block(Rectangle):
    # do something here

# class Shape(object):
    # do something here

# class  I_shape(Shape):
#   def  __init__(self,  center):
#     coords  =  [Point(center.x  -  1,  center.y),
#                 Point(center.x  ,  center.y),
#                 Point(center.x  +  1,  center.y),
#                 Point(center.x  +  2,  center.y)]
#     Shape.__init__(self,  coords,  "blue")
#     self.center_block = self.blocks[1]

# class J_shape(Shape):
    # do something
# class L_shape(Shape):
    # do something
# class O_shape(Shape):
    # do something
# class S_shape(Shape):
    # do something
# class T_shape(Shape):
    # do something
# class Z_shape(Shape):
    # do something

# create a window to draw the tetronimoes
win = GraphWin("Tetronimoes", 150, 150)

# the block is drawn at position (1,1) on the board
block = Block(Point(1,1), 'red')
block.draw(win)

# keep this last!
win.mainloop()
