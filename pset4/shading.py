# shading.py

# Name:
# Collaborators:

# This draws a shaded sphere on the screen.

from graphics import *
from time import sleep   # for pausing between frames

win = GraphWin("Ball", 300, 300)

# sphere location and radius
x = 150
y = 150
r = 100

# control for lighting, resolution, and flatness
dx = 1
dy = 1
dr = 2

while r > 0:
    # find the arguments for the new circle
    r = r - dr
    x = x - dx
    y = y - dy

    # draw a new circle
    c = Circle(Point(x, y), r)
    rgb = 255 - ((255 * r) / 100)
    c.setFill(color_rgb(rgb, rgb, rgb))
    c.setOutline(color_rgb(rgb, rgb, rgb))
    c.draw(win)
    
win.mainloop()
