# concentration.py

# Name: 
# Collaborators:

# This lets users play a game of concentration.

from graphics import *
import random
from time import sleep

# FILL THIS IN: Waits for user to click on a card and returns the card location
def get_card() :
    pass

# FILL THIS IN: Checks if the game is over
def is_game_over() :
    pass

# graphics variables
CARD_WIDTH = 50
CARD_HEIGHT = 80

win = GraphWin("Concentration",4*CARD_WIDTH, 4*CARD_HEIGHT)

# shuffle the cards
all_cards = range(8)*2
random.shuffle(all_cards)

# FILL THIS IN: Make a dictionary for storing the cards

# color values
c = ['red','green','blue','yellow','purple','cyan','brown','white']

for i in range(16) :
    row = i/4
    col = i%4
    
    # draw the cards
    r = Rectangle(Point(row*CARD_WIDTH, col*CARD_HEIGHT),Point((row+1)*CARD_WIDTH,(col+1)*CARD_HEIGHT))
    r.setFill(c[all_cards[i]])
    r.setOutline('white')
    r.draw(win)

    # FILL THIS IN: Store the card in a dictionary

# Your main code block goes here
    
win.mainloop();
