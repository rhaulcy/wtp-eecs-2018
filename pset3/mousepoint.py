# mousepoint.py

# Name :
# Collaborators :

# Retrieves the mouse pointer coordinates

from graphics import *

# create the graphics window
win = GraphWin("Mouse Pointer", 300, 300)

# TODO: add your code to draw the rectangle!

# get mouse coordinates
while True:
    # we will learn more about while loops next lecture
    # for now all your code must be within this loop,
    #   without the loop you would only be able to click once! 
    p = win.getMouse()
    x = p.getX()
    y = p.getY()
    print 'x: ', x, ', y: ', y
    
    # TODO: add your code here! 
	#   check if the point is inside


# process events (don't change/move this)
win.mainloop()
