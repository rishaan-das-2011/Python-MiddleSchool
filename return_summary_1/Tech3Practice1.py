"""
LESSON: 6.3 - Complex Parameters
TECHNIQUE 3: Return Summary
PRACTICE 1
"""

#### ---- LIBRARIES ---- ####
import random

#### ------------------------------------- ####
#### ---- CREATE RANDOM WORD FUNCTION ---- ####
#### ------------------------------------- ####
def make_random_word():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    word = []

    # Pick 10 letters at random
    for i in range(10):
        word.append(random.choice(alphabet))

    return word


#### --------------------------------- ####
#### ---- PRINTABLE WORD FUNCTION ---- ####
#### --------------------------------- ####
def printable_word(list):
    word = ""
    for letter in list:
        word += letter

    return word


#### ---------------------------------- ####
#### ---- REPLACE LETTERS FUNCTION ---- ####
#### ---------------------------------- ####
def replace_letters(blank_list, word_letters, guess):

    # Track whether a letter has been found or not

    found = False

    for i in range(len(blank_list)):
        if word_letters[i] == guess and blank_list[i] == "_":

            # We found a new letter
            blank_list[i] = word_letters[i]
            found = True


    # Return whether a new letter was found

    return found

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

#### ---- GAME SETUP ---- ####
# Starting lists
word = make_random_word()
blanks = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
guesses = 15
guessed = []


#### ---- GUESS LOOP ---- ####
while guesses > 0:

    # Print current game state
    print("Current word: " + printable_word(blanks))
    print("Guessed Letters: " + str(guessed))

    print()
    print("You have " + str(guesses) + " guesses remaining.")
    letter = input("Guess a letter: ")
    print()

    # Make sure we haven't already guessed this letter
    if not letter in guessed:

        # Test guess
        got_found = replace_letters(blanks, word, letter)
        guessed.append(letter)

        # Only reduce the number of guesses left on an
        # incorrect guess
        if not got_found:
            guesses -= 1

    # If we already guessed, let the user know
    else:
        print("You already guessed that letter. Try again.")

    # If we guessed the whole word, we can stop
    if not "_" in blanks:
        print("Wow! You guessed it! Congratulations!")
        break


#### ---- FINAL OUTPUT ---- ####
if guesses == 0:
    print("Sorry, the correct word was: " + printable_word(word))


# Turn in your Coding Exercise.
