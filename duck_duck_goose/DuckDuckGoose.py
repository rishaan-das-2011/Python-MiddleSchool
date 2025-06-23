"""
LESSON: 4.1 - Lists
EXERCISE: Duck Duck Goose
"""

#### ---- SETUP ---- ####

# --- Libraries --- #

# Import random library

import random

# Import pygame library

import pygame

# Initialize pygame library

pygame.init()

# --- Variables --- #

# Create a variable select_list and assign it a LIST
# containg at least 5 "duck" strings and 1 "goose"
# ---> TEST AFTER THIS LINE <--- #

select_list = ["Duck", "Duck", "Duck","Duck", "Duck", "Goose"]

# Create a variable pick and assign it "duck"

Pick = "Duck"

#### ---- MAIN LOOP ---- ####

# Loop while pick is not equal to "goose"

while Pick != "Goose":

    # --- Get random entry --- #

    # Get a randint between 0 and the LEN of
    # select_list - 1. assign the value to index
    # ---> TEST AFTER THIS LINE <--- #

    index = random.randint(0, len(select_list)-1)

    # Get item at INDEX position index from list
    # select_list and assign it to pick
    # ---> TEST AFTER THIS LINE <--- #

    Pick = select_list[index]

    # --- Pause --- #

    # Wait for 1500 milliseconds
    # ---> TEST AFTER THIS LINE <--- #

    pygame.time.wait(1500)

    # --- Check what word you got --- #

    # If pick is equal to "duck"
    
    if Pick == "Duck":

        # Print "Duck..."
        print("Duck...")

    # Else
    else:

        # Print "Goose!"
        # ---> TEST AFTER THIS LINE <--- #
        print("Goose!")
        break





# Turn in your Coding Exercise.

