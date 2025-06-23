"""
LESSON: 5.1 - Sprites
EXERCISE: Mystic Mirror
"""

#### ---- SET UP ---- ####

# --- Libraries --- #

# Import the tsk library

import tsk

# Import the pygame library

import pygame

# Initialize pygame

pygame.init()

# --- Animation variables --- #

# Open a new window of size [1018, 573] and assign to
# window


window = pygame.display.set_mode([1018, 573])

# Create a new SPRITE object for the stage
# using "stage.png" at (0, 0)

stage = tsk.Sprite("stage.png", 0, 0)

# Create a new SPRITE object for the curtains
# using "curtain.png" at (0, 0)

curtain = tsk.Sprite("curtain.png", 0, 0)

# Create a new SPRITE object for the mirror
# using the "mirror.png" image at (800, 0)

mirror = tsk.Sprite("mirror.png", 800, 0)

# Create a new SPRITE object for the gem
# using the "gem.png" image at (400, 200)

gem = tsk.Sprite("gem.png", 400, 200)

# --- Image input --- #

# Declare a boolean called transformed, set to False

transformed = False

# Print an introductory line saying that you're going
# to cast a spell using a magic mirror

print("I am going to cast a spell using a magic mirror! ")

# Print the options for images to transform the gem
# into: "harp.png", "magical_bird.png"
# "googly_eye_stone.png", and "bee_pug.png"

print("Options: harp.png, magical_bird.png, googly_eye_stone.png, bee_pug.png")

# Ask the user to input which image to transform
# the gem into, and store as target

target = input("Which image should the gem transform into? ")

# --- Loop variables --- #

# Create a variable called drawing and assign it True

drawing = True

#### ---- MAIN LOOP ---- ####

# Loop while drawing

while drawing:

    # --- Event loop --- #

    # Create an event loop

    for event in pygame.event.get():

        #  If the event is equal to the QUIT event

        if event.type == pygame.QUIT:

            # Set drawing to False

            drawing = False

    # --- Moving mirror --- #

    # Decrement the mirror's CENTER_X by 6

    mirror.x -= 6

    # --- Transforming --- #

    # If the mirror's CENTER_X is less than the
    # gem's CENTER_X and transformed is False

    if mirror.x < gem.x and not transformed:

        # Set the gem's IMAGE to target

        gem.image = target
        
        # Set transformed to True

        transformed = True
    
        # Print a message that the spell is done

        print("The spell is completed! ")

    # --- End program --- #

    # If the mirror's CENTER_X is less than -300

    if mirror.x < -300:

        # Set drawing to False
        # ---> TEST AFTER THIS LINE <--- #

        drawing = False

    # --- Drawing --- #

    # DRAW the stage

    stage.draw()

    # DRAW the gem

    gem.draw()

    # DRAW the mirror

    mirror.draw()

    # DRAW the curtains

    curtain.draw()

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #

    pygame.display.flip()
    
    
# Turn in your Coding Exercise.