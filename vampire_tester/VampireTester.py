"""
LESSON: 4.1 - Lists
EXERCISE: Vampire Tester
"""

#### ---- SETUP ---- ####

# IMPORT the random library

import random

# Create an empty LIST and assign to variable people
# (Hint: an empty list has nothing inside the [])
# ---> TEST AFTER THIS LINE <--- #

people = []

# Create a variable called name and assign it an empty
# string

name = ""

#### ---- input LOOP ---- ####

# While name is not equal to "done"

while name != "done":

    # --- Add new name to list --- #

    # Get a name or "done" as input and assign to
    # variable name
    
    name = input("Enter a name (or 'done' to finish): ")

    # If name is equal to "done"

    if name == "done":

        # break
        # ---> TEST AFTER THIS LINE <--- #

        break

    # APPEND name to the people list
    # ---> TEST AFTER THIS LINE <--- #

    people.append(name)

# --- Pick who the vampire is --- #

# Get a RANDINT between 0 and the LEN of people - 1 and
# assign to variable pick

pick = random.randint(0, len(people) - 1)

# Use pick as an INDEX to get a value from the list
# people and assign that to the variable vampire
# ---> TEST AFTER THIS LINE <--- #

vampire = people[pick]

# Print a blank line

print()

#### ---- GUESSING LOOP ---- ####

# While the LEN of people is greater than 1

while len(people) > 1:

    # --- User guess --- #

    # Print the people list typecasted to a string as
    # part of a message

    print("People " + str(people))

    # Ask the user to input who they think the vampire
    # is and assign the result to guess

    guess = input("Who do you think is the vampire?")

    # --- Check for correct answer --- #

    # If guess and vampire are equal

    if guess == vampire:

        # Print a congratulations message

        print("Congratulations! You have found the vampire")

        # break
        break


    # --- Remove incorrect guess --- #

    # Elif guess is IN list people

    elif guess in people:

        # Print that the user was incorrect

        print("Sorry, that is not the vampire.")

        # REMOVE guess from list people
        # ---> TEST AFTER THIS LINE <--- #

        people.remove(guess)

    # Print a blank line for readability

    print()

#### ---- FINAL OUTPUT ---- ####

# If LEN of people is equal to 1

if len(people) == 1:

    # Print a message that the user didn't get it.
    # Include the variable vampire.
    # ---> TEST AFTER THIS LINE <--- #

    print("Game over! You failed to find the vampire. The vampire was " + vampire + ".")




# Turn in your Coding Exercise.
