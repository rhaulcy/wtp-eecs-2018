# wheel.py

# Name :
# Collaborators :

# Program for drawing a moving wheel

from graphics import *

class Wheel(object):
        def __init__(self, center, wheel_radius, tire_radius):
                self.tire_circle = Circle(center, tire_radius)
                self.wheel_circle = Circle(center, wheel_radius)
        def draw(self, win):
                self.tire_circle.draw(win)
                self.wheel_circle.draw(win)
        def move(self, dx, dy):
                self.tire_circle.move(dx, dy)
                self.wheel_circle.move(dx, dy)
        def set_color(self, wheel_color, tire_color):
                self.tire_circle.setFill(tire_color)
                self.wheel_circle.setFill(wheel_color)
        def undraw(self):
                self.tire_circle.undraw()
                self.wheel_circle.undraw()
        def get_size(self):
                return self.tire_circle.getRadius()
        def get_center(self):
                return self.tire_circle.getCenter()

win = GraphWin('Wheel', 320, 240)
w = Wheel(Point(100, 100), 50, 70)
w.draw(win)
w.set_color('gray', 'black')
w.animate(win, 1, 0, 100)
#w.undraw()

win.mainloop()
