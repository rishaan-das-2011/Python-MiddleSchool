"""
LESSON: 5.1 - Sprites
EXERCISE: Growing Down
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

# Create a new SPRITE object for the background using
# the "ScienceLabWithShrinkRay.jpg" image at (0, 0)

BG = tsk.Sprite("ScienceLabWithShrinkRay.jpg", 0, 0)

# Create a new SPRITE object for the panda using the
# "Panda.png" image at (0, 0)

panda = tsk.Sprite("Panda.png", 0, 0)

# Position the panda sprite's CENTER near the
# middle of the screen, at (509, 250)

panda.center = (509, 250)

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
            # ---> TEST AFTER THIS LINE <--- #

            drawing = False

        # --- Keyboard input --- #

        # Else if event.type is KEYDOWN and the
        # event.key is K_LEFT

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: 


            # Decrement the panda's CENTER_X by 20
            x, y = panda.center
            panda.center = (x - 20, y)
            
        # Else if event.type is KEYDOWN and the
        # event.key is K_RIGHT

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:

            # Increment the panda's CENTER_X by 20
            # ---> TEST AFTER THIS LINE <--- #
            x, y = panda.center
            panda.center = (x + 20, y)
    
        # Else if event.type is KEYDOWN and the
        # event.key is K_DOWN

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:

            # Decrement the panda's SCALE by 0.05

            panda.scale -= 0.05

            # Increment the panda's CENTER_Y by 10
            # ---> TEST AFTER THIS LINE <--- #
            x, y = panda.center
            panda.center = (x, y + 10)

    # --- Setting panda size --- #

    # If the panda's SCALE is less than 0.1

    if panda.scale < 0.1:

        # Set the panda SCALE to 0.1
        # ---> TEST AFTER THIS LINE <--- #

        panda.scale = 0.1

    #### ---- DRAW OUTPUT ---- ####

    # DRAW the background

    BG.draw()

    # DRAW the panda

    panda.draw()

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #

    pygame.display.flip()
    
    
# Turn in your Coding Exercise.    