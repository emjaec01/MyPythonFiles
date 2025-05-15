#Day 7 Project:Hangman
import random
from hangman_art import hangman_logo
'''
FLOW OF THE GAME:
1. Start
2. Generate a random word
3. Generate as many blanks as letters in word
4. Ask the user to guess a letter.
5. Is the guessed letter in the word?
    yes - replace the blank with the letter
    no - lose a life
5.1. Are all the blanks filled?
    no - go back to #4
    yes - game over.
5.2. Have they run out of lives?
    no - go back to #4
    yes - game over.

word_list=['emjae', 'jemmar', 'joseph']
'''
print(hangman_logo)
#Steps in creating the game.
################################################################################
#Step 1-Picking a random words and checking answers
################################################################################
#TODO-1 - Randomly choose a word from the world_list and assign it  to a variable called chosen_word. Then print it.
'''
chosen_word = random.choice(word_list)
print(chosen_word)
'''
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
'''
guess=input("Guess a letter: ").lower()
print(guess)
'''
#TODO-3 - Check if the letter the user guessed is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.
'''
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
'''
################################################################################
#Step 2-Replacing Blanks with Guesses
################################################################################
#TODO-1 - Create a "placeholder" with the same number of blanks as the chosen_word
'''
placeholder=""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()
'''
#TODO-2 - Create a "display" that puts the guess letter in the right position and _ in the rest of the string.
'''
display=""
for letter in chosen_word:
     if letter == guess:
        display += letter
    else:
        display += "_"
print(display)
'''
################################################################################
#Step 3 - Checking if the Player has Won
################################################################################
#TODO-1 - Use a while loop to let the user guess again.
'''
correct_letters=[]
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
'''
#TODO-2 - Change the for loop so that you keep the previous correct guessed.
'''
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")
'''
################################################################################
#Step 4 - Keeping Track of the Player's Lives
################################################################################
hangman = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']
#TODO-1 - Create a variable called 'lives' to keep track of the number of lives left.
# Set lives = 6
lives=6
word_list=['emjae', 'jemmar', 'joseph']
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
correct_letters=[]
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f'You\'ve already guessed {guess}')
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

#TODO-2 - If guess is not a letter in the chosen_word, Then reduce lives by 1.
# If lives goes down to 0 then the game should end, and it should print "You lose."

    if "_" not in display:
        game_over = True
        print("You win.")

    if guess not in chosen_word:
        lives -=1
        print(f'The \'{guess}\' is not in the word. You lose a life.')
        if lives ==0:
            game_over=True
            print(f'{"*"*15}YOU LOSE{"*"*15}')
    if "_" not in display:
        game_over = True
        print(f'{"*"*15}YOU WIN{"*"*15}')

#TODO-3 - print the ASCII art from 'stages'
# that corresponds to the current number of 'lives' the user has remaining.
    print(f'{"*"*15}YOU HAVE {lives}/6 LIVES LEFT{"*"*15}')
    print(hangman[lives])

