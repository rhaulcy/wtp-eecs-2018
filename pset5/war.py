# war.py

# Name:
# Collaborators:

# This lets the user play a game of war

from queue import *
import random

# initializes player1 and player2 queues
player1 = Queue()
player2 = Queue()

# list of cards
cards = [2,2,2,2,3,3,3,3,4,4,4,4,
         5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,
         9,9,9,9,10,10,10,10,11,11,11,11,
         12,12,12,12,13,13,13,13,14,14,14,14]

# Divide cards between 2 players. Should return initialized player queues
def shuffle(cards, player1, player2):
    # YOUR CODE HERE
    pass

# write the game. calls shuffle to initialize players at beginning.
def play():
    # initializes p1 and p2
    p1, p2 = shuffle(cards, player1, player2)

   # YOUR CODE HERE
   pass

# check if the game is over
def is_game_over():
    # YOUR CODE HERE
    pass


# print winner
def print_winner():
    # YOUR CODE HERE
    pass

