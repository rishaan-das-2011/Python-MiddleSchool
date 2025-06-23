"""
LESSON: 5.4 - Sprites in Lists
EXERCISE: Bee Plus
"""

#### ---- SET UP ---- ####

# --- Libraries ---  #

# Import the tsk library

import tsk

# Import the random library

import random

# Import the pygame library

import pygame

# Initialize pygame

pygame.init()

# --- Variables --- #

# Open a new window of size [1018, 573] and assign to
# window

window = pygame.display.set_mode([1018, 573])

# Create a new Clock and assign to c

c = pygame.time.Clock()

# Create a SPRITE called background using
# "FlowerMeadow.jpg" at (0, 0)

background = tsk.Sprite("FlowerMeadow.jpg", 0, 0)

# Create a SPRITE called beehive using "Beehive.png"
# at (-80, 70)

beehive = tsk.Sprite("Beehive.png", -80, 70)

# Create a SPRITE called flowerbush using
# "Bush.png" at (620, 250)

flowerbush = tsk.Sprite("Bush.png", 620, 250)

# Create an empty list called bees_leaving

bees_leaving = []

# Create an empty list called bees_returning

bees_returning = []

# Create a variable called bee_spawn_time, set to 1000

bee_spawn_time = 1000

# Create a variable called timer, set to 0

timer = 0

# Create a variable called bee_speed, set to 0.2

bee_speed = 0.2

# Create a variable called maximum_bees, set to 10

maximum_bees = 10

#### ---- MAIN LOOP ---- ####

# Create a variable called drawing, set to True

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

    # ---- Spawn new bees ---- #

    # Increment the timer by c.get_time()

    timer += c.get_time()

    # If the timer is greater than the bee_spawn_time

    if timer > bee_spawn_time:

        # Reset the timer to 0

        timer = 0

        # If the length of bees_leaving + the length
        # of bees_returning is less than maximum_bees

        if len(bees_leaving) + len(bees_returning) < maximum_bees:

            # Create a SPRITE called bee using
            # "Bee.png" at the beehive's center_x and
            # a random y between 200 and 350

            bee = tsk.Sprite("Bee.png", beehive.center_x, random.randint(200, 350))

            # Append bee to the list of bees_leaving
            # ---> TEST AFTER THIS LINE <--- #

            bees_leaving.append(bee)

    # ---- Move bees ---- #

    # For every bee in the list of bees_leaving

    for bee in bees_leaving:

        # Increment bee's CENTER_X by
        # bee_speed * c.get_time()

        bee.center_x += bee_speed * c.get_time()

        # If the bee's CENTER_X is greater than the
        # flowerbush's CENTER_X

        if bee.center_x > flowerbush.center_x:

            # Set the bee's flip_x to True

            bee.flip_x = True

            # Remove the bee from bees_leaving

            bees_leaving.remove(bee)

            # Append the bee to bees_returning
            # ---> TEST AFTER THIS LINE <--- #

            bees_returning.append(bee)

    # Create an empty list called done_bees

    done_bees = []

    # For every bee in the list of bees_returning

    for bee in bees_returning:

        # Decrement bee's CENTER_X by
        # bee_speed * c.get_time()

        bee.center_x -= bee_speed * c.get_time()
        
        # If the bee's CENTER_X is less than the
        # beehive's CENTER_X

        if bee.center_x < beehive.center_x:

            # Append the bee to done_bees

            done_bees.append(bee)

    # For every bee in done_bees

    for bee in done_bees:

        # Remove the bee from bees_returning
        # ---> TEST AFTER THIS LINE <--- #

        bees_returning.remove(bee)


    # --- Draw --- #

    # DRAW the background

    background.draw()

    # DRAW the beehive

    beehive.draw()

    # DRAW the flowerbush

    flowerbush.draw()

    # For each bee in bees_leaving

    for bee in bees_leaving:

        # DRAW the bee

        bee.draw()

    # For each bee in bees_returning

    for bee in bees_returning:

        # DRAW the bee

        bee.draw()

    # Flip the display

    pygame.display.flip()

    # Tick c at 30 framerate
    # ---> TEST AFTER THIS LINE <--- #

    c.tick(30)





# Turn in your Coding Exercise.
