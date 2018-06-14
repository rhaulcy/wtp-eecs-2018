# tictactoe.py

# Name:
# Collaborators: 


# your code here

# save the state of the board (empty at first)
board_state = ["","","","","","","","",""]

######## HELPER FUNCTIONS ######
# draw the Tic-Tac-Toe board
def draw_board():
    # your code here
    pass

# draw an X at the (i,j)th square on the board
def draw_X(i, j):
    # your code here
    pass

# draw an O at the (i,j)th square on the board
def draw_O(i, j):
    # your code here
    pass

# returns True if (i,j)th square is empty; False otherwise
def is_empty(i, j):
    # your code here
    pass

# returns True if the entire board is full; False otherwise
def is_board_full():
    # your code here
    pass

# updates the board state when player plays in (i,j)th square
def update_board_state(i, j, player):
    # player variable should be the string "X" or "O"
    # your code here
    pass

# check the board for the ways the game could be over (included winning conditions)
def is_over():
    # your code here
    pass

#### ACTUAL GAMEPLAY ######
# create a window

# draw the board

# save which player goes first (X or O, it doesn't matter)

# Have players take turns. For each player's turn (until the game ends):
# - save where the mouse click was
# - figure out which square the player chose
# - if the square is not taken, update the board state and draw the symbol

