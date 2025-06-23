"""
LESSON: 5.4 - Sprites in a List
EXERCISE: Buried Treasure
"""

#### ---- SET UP ---- ####

# --- Libraries ---  #

# Import the tsk library

import tsk

# Import the pygame library

import pygame

# Import the random library

import random

# Initialize pygame

pygame.init()

# --- Variables --- #

# Open a window of size [1018, 573] called window

window = pygame.display.set_mode([1018, 573])

# Create a SPRITE called ground using "DugHole.jpg"
# at (0, 0)

ground = tsk.Sprite("DugHole.jpg", 0, 0)

# Create a SPRITE called treasure using "Treasure.png"
# (300, 150)

treasure = tsk.Sprite("Treasure.png", 300, 150)

# Create an empty list called dirt

dirt = []

# --- Dirt sprite creation loop --- #

# For i in range 30

for i in range (30):

    # Create a SPRITE object called dirt_sprite using
    # "DirtMound.png" with a random x between 0 and
    # 587 and a random y between 100 and 500.

    dirt_sprite = tsk.Sprite("DirtMound.png", random.randint(0, 587), random.randint(100, 500))

    # Append dirt_sprite to the dirt list
    # ---> TEST AFTER THIS LINE <--- #

    dirt.append(dirt_sprite)

#### ---- MAIN LOOP ---- ####

# Create a variable called drawing and assign it True

drawing = True

# Loop while drawing

while drawing:

    # --- Event loop --- #

    # Create an event loop

    for event in pygame.event.get():

        #  If the event is equal to the QUIT event

        if event.type == pygame.QUIT:

            # Set drawing to False
            # ---> TEST AFTER THIS LINE <--- #

            drawing = False

        # --- Keyboard input --- #

        # Elif the event type is KEYDOWN

        elif event.type == pygame.KEYDOWN:

            # If the length of the dirt  list
            # is greater than 0

            if len(dirt) > 0:

                # Remove dirt_sprite from the dirt list
                # ---> TEST AFTER THIS LINE <--- #

                dirt_sprite = dirt.pop()





    # --- Draw --- #

    # DRAW the ground

    ground.draw()

    # DRAW the treasure

    treasure.draw()

    # For every sprite in the dirt list

    for sprite in dirt:

        # DRAW that sprite

        sprite.draw()

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #

    pygame.display.flip()


# Turn in your Coding Exercise.
