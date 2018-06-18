# WTP CS Problem Set 8.1 - Hangman: Day 1

To get started, log into your Edmodo student account, find the post for Problem Set 8.1, and download the files.

For this pset, you’ll be coding a small hangman game! Today, you’ll code the game and rules without graphics, and tomorrow, you’ll add classic hangman images.

Rules:
- Player 1 will think of a word.
- Player 2 will guess letters she suspects would be in the word.
- Game Over Conditions:
  - If player 2 guesses incorrectly 6 times, the game is over. Player 1 wins
  - If player 2 guesses all the letters in the word, player 2 wins
- Player 2 can only guess a letter once. (i.e if player 2 guesses an incorrect letter twice, they should be forced to guess again without penalty)
- After every new letter guessed, display the word but with underscores replacing every letter that has not been guessed by player 2.
 
### 1. Warm up - Input: 
Open `hangman.py` and write a program that asks for both players' names, and prints ` Hello <name>!`
When you run it in the terminal, it should look something like:
```python
What is player 1's name? <type in name>
What is player 2's name? <type in name>
Hello <player 1>!
Hello <player 2>!
```
 
### 2. Helper Function - Display: 
Fill in the `display` function in `hangman.py` that will display the word as a string of underscores and letters. For example, if you type the first three lines below into a python console, it should produce the fourth line:
```python
>>> word = “butterscotch”
>>> letters = [‘a’, ‘g’, ‘r’, ‘t’]
>>> display(letters, word)
“ _ _ t t _ r _ _ _ t _ _”
```
 
### 3. Initial Guiding Questions:
After player 1 inputs a word, what information do you need to keep track of to determine if player 2 can guess again?

*Hint: For example, how can you keep track of how many letters in the word have been guessed?*
 
### 4. Conditional Guiding Questions:
After player 2 guesses a letter, what are the different cases that could occur?

*Hint: Ask yourself, if this happens, then what follows?*
 
### 5. Termination Guiding Questions:
How do you know when to end the game?    

*Hint: How can you get an input from the user multiple times without repeating code? (And when do you 
    stop?)*
    
### 6. Testing
After your game is finished, play it a few times and see if you find any bugs that you need to fix. For example, does your game work if Player 1 enters a word that has capital letters in it?

**Please make sure to add comments to your code explaining what you are doing!**

### 6. Challenge (Optional): 
Make the game replayable and keep track of the score for players 1 and 2!

*Tip: If you start a program and can't figure out how to end it, press control + C to terminate.*

### Submitting your PSET
After you’ve finished your PSET, log into your Edmodo account, find the post for Problem Set 8.1, click "Open Assignment", attach all of the files that you created or edited for Problem Set 8.1, and then click "Turn in Assignment". You can resubmit the assignment as many times as you'd like. After you turn in your assignment, you're all done!
