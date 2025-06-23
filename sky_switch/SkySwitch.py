"""
LESSON: 5.3 - Sprite Collision
EXERCISE: Sky Switch
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

# Open a new window of size [1018, 573] and assign to
# window

window = pygame.display.set_mode([1018, 573])

# Create a SPRITE called background with the image
# "HillsGrassy.png" at 0, 0

hills = tsk.Sprite("HillsGrassy.png", 0, 0)

# Create a SPRITE called clouds with the image
# "Clouds.png" at 0, 0

clouds = tsk.Sprite("Clouds.png", 0, 0)

# Create a SPRITE called switch with the image
# "LightSwitch.png" at 50, 50

light = tsk.Sprite("LightSwitch.png", 50, 50)

# Create a variable called sky_color set to blue

sky_color = (0, 0, 255)

#### ---- MAIN LOOP ---- ####

# Create a variable called drawing and assign it True

drawing = True

# Loop while drawing

while drawing:

    # --- Event loop --- #

    # Create an event loop

    for event in pygame.event.get():   

        # If the event is equal to the QUIT event

        if event.type == pygame.QUIT:

            # Set drawing to False
            # ---> TEST AFTER THIS LINE <--- #

            drawing = False

        # --- Mouse input --- #

        # Elif the event type is MOUSEBUTTONDOWN

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Store the mouse position in x, y

            x, y = pygame.mouse.get_pos()

            # Use COLLIDEPOINT to see if the mouse
            # overlaps with the switch

            if light.rect.collidepoint(x, y):

                # Make a new integer called red, set
                # to a random value between 0 and 255

                red = random.randint(0, 255)

                # Make a new integer called green, set
                # to a random value between 0 and 255

                green = random.randint(0, 255)

                # Make a new integer called blue, set
                # to a random value between 0 and 255

                blue = random.randint(0, 255)

                # Set sky_color to a new tuple made
                # with red, green, and blue
                # ---> TEST AFTER THIS LINE <--- #

                sky_color = (red, green, blue)


    # --- Draw --- #

    # Fill the window with the sky_color

    window.fill(sky_color)

    # DRAW the background

    hills.draw()

    # DRAW the clouds

    clouds.draw()

    # DRAW the switch

    light.draw()

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #

    pygame.display.flip()
    
    
    
# Turn in your Coding Exercise.
