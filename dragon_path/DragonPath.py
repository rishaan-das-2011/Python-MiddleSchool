"""
LESSON: 5.2 - Spritesheet Animation
EXERCISE: Dragon Path
"""

#### ---- SET UP ---- ####

# --- Libraries --- #

# Import the tsk library

import tsk

# Import the pygame library

import pygame

# Initialize pygame

pygame.init()

# --- Program variables --- #

# Open a window of size [1018, 573] and assign to
# window

window = pygame.display.set_mode([1018, 573])

# Create a new Clock and assign to c

c = pygame.time.Clock()

# --- Sprites --- #

# Create a new SPRITE called background using
# "FantasyPlains.jpg" at 0, 0

plains = tsk.Sprite("FantasyPlains.jpg", 0, 0)

# Create a new IMAGESHEET called wiz_sheet using the
# "WizardWalking.png" image with 4 rows and 6 columns.
# ---> TEST AFTER THIS LINE <--- #

wiz_sheet = tsk.ImageSheet("WizardWalking.png", 4, 6)

# Create a new SPRITE called wizard with wiz_sheet at
# 150, 280

wizard = tsk.Sprite(wiz_sheet, 150, 280)

# Create a new IMAGESHEET called dragon_sheet using the
# "DragonFlying.png" image with 4 rows and 6 columns.

dragon_sheet = tsk.ImageSheet("DragonFlying.png", 4, 6)

# Create a new SPRITE called dragon with dragon_sheet
# at 650, 30

dragon = tsk.Sprite(dragon_sheet, 650, 30)

# Set the wizard's IMAGE_ANIMATION_RATE to 30

image_animation_rate = 30

# --- Timing Variables --- #

# Create a variable called appearing with value False

appearing = False

# Create a variable called dragon_timer, set to 0

dragon_timer = 0

# Create a new variable called appear_time, set to 2000

appear_time = 2000

# Create a new variable called hide_time, set to 3000

hide_time = 3000

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

    # --- Update timer --- #

    # Increment dragon_timer by get_time

    dragon_timer += c.get_time()

    # If the dragon is appearing and dragon_timer
    # is greater than appear_time

    if appearing and dragon_timer > appear_time:
        
        # Set dragon_timer to 0

        dragon_timer = 0

        # Set appearing to False
    
        appearing = False

    # If the dragon is not appearing and dragon_timer
    # is greater than hide_time

    if not appearing and dragon_timer > hide_time:

        # Set dragon_timer to 0

        dragon_timer = 0

        # Set appearing to True
        # ---> TEST AFTER THIS LINE <--- #

        appearing = True

    # --- Move with arrow keys --- #

    # If not appearing

    if not appearing:

        # If the right arrow key is down

        if tsk.get_key_pressed(pygame.K_RIGHT):

            # Increment wizard's x by .1 * c.get_time()

            wizard.x += 0.1 * c.get_time()

            # Set the wizard's flip_x to False

            wizard.flip_x = False

        # If the left arrow key is down

        if tsk.get_key_pressed(pygame.K_LEFT):

            # Decrement wizard's x by .1 * c.get_time()

            wizard.x -= 0.1 * c.get_time()

            # Set the wizard's flip_x to True
            # ---> TEST AFTER THIS LINE <--- #

            wizard.flip_x = True

    # --- Animate --- #

    # If the dragon is appearing

    if appearing:

        # Set the wizard's IMAGE_ANIMATION_RATE to 0

        wizard.image_animation_rate = 0

    # Else


    else:
        
        # Set the wizard's IMAGE_ANIMATION_RATE to 30

        wizard.image_animation_rate = 30

    # UPDATE the dragon's animation with c.get_time()

    dragon.update(c.get_time())

    # UPDATE the wizard's animation with c.get_time()

    wizard.update(c.get_time())

    # ---  Draw --- #

    # DRAW the background

    plains.draw()

    # If the dragon is appearing

    if appearing:

        # DRAW the dragon
    
        dragon.draw()

    # DRAW the wizard

    wizard.draw()

    # Flip the display
    
    pygame.display.flip()

    # Tick the clock by 30
    # ---> TEST AFTER THIS LINE <--- #


    c.tick(30)


# Turn in your Coding Exercise.
