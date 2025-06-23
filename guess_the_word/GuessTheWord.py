"""
LESSON: 4.3 - For Range
EXERCISE: Guess the Word
"""

#### ---- SETUP ---- ####

# Assign variable guesses the value 6

guesses = 6

# Assign variable wrong_letters an empty LIST

wrong_letters = []

# Assign variable right_letters an empty LIST

right_letters = []

#### ---- WORD SELECTION ---- ####

# --- Get user input --- #

# Ask the user to input a word, assign to variable word
# ---> TEST AFTER THIS LINE <--- #

word = input("Enter a word: ")

# --- Blank the screen --- #

# Print 100 blank lines (Hint: Use "\n")
# ---> TEST AFTER THIS LINE <--- #

print('\n' * 100)
    
# --- Create blanks for each letter in word --- #

# FOR each letter in word

for letter in word:

    # APPEND "_" to list right_letters
    # ---> TEST AFTER THIS LINE <--- #

    right_letters.append("_")

#### ---- GUESSING LOOP ---- ####

# While "_" is IN right_letters and guesses is
# greater than 0

while "_" in right_letters and guesses > 0:

    # Print "You have guessed: " + wrong_letters
    # typecasted to a string

    print("You have guessed: " + str(wrong_letters))

    # Print "Word: " + right_letters typecasted to a
    # string

    print("Word: " + str(right_letters))

    # Print how many guesses remain

    print("You have " + str(guesses) + " left. ")

    # Ask user to input a letter and assign to guess

    guess = input("Input a letter: ") 

    # Print a blank line

    print()

    #### ---- CHECK GUESS ---- ####

    # If guess is not IN wrong_letters and guess is not
    # IN right_letters

    if guess not in wrong_letters and guess not in right_letters:

        # Assign variable found the value False

        found = False

        # --- If any letters in the word are the one
        # the user guessed, replace blanks --- #

        # FOR i in RANGE LEN of word

        for i in range(len(word)):

            # If INDEX i of word is equal to guess

            if word[i] == guess:

                # Assign right_letters at INDEX i the
                # value guess

                right_letters[i] = guess

                # Assign found the value True
                # ---> TEST AFTER THIS LINE <--- #

                found = True

        # --- Otherwise, player loses a guess --- #

        # If not found

        if not found:

            # Decrement guesses by 1

            guesses -= 1

            # APPEND guess to wrong_letters list
            # ---> TEST AFTER THIS LINE <--- #

            wrong_letters.append(guess)

    # Else

    else:

        # Print "You guessed that letter already"
        # ---> TEST AFTER THIS LINE <--- #

        print("You have guessed that letter already.")

#### ---- FINAL OUTPUT ---- ####

# If "_" is not IN right_letters

if "_" not in right_letters:

    # Print a congratulations message
    # ---> TEST AFTER THIS LINE <--- #

    print("Congratulations! You have guessed the word.")

# Else

else:

    # Print "Sorry, you didn't guess it"
    # ---> TEST AFTER THIS LINE <--- #

    print("Sorry, you didn't guess it. The world was: " + word)



# Turn in your Coding Exercise.





