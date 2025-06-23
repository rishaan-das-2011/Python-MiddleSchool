"""
LESSON: 6.3 - Complex Parameters
EXERCISE: Impending Doof
"""

#### ---- LIBRARIES ---- ####

# Import the tsk library

import tsk

# Import the pygame library

import pygame

# Initialize the pygame library

pygame.init()

#### ------------------------------- ####
#### ---- MOVE TOWARDS FUNCTION ---- ####
#### ------------------------------- ####

# DEFINE the move_towards function with PARAMETERS
# sprite, goal, and speed

def move_towards(sprite, goal, speed):

    # Assign goal_x, goal_y the values from goal

    goal_x, goal_y = goal

    # --- Move left and right --- #

    # If goal_x is less than the sprite's center_x - 50

    if goal_x < sprite.center_x - 50:

        # Set the sprite's flip_x to True

        sprite.flip_x = True

        # Decrement the sprite's center_x by speed
        # ---> TEST AFTER THIS LINE <--- #

        sprite.center_x -= speed

    # Else if goal_x is greater than the sprite's
    # center_x + 50

    elif goal_x > sprite.center_x + 50:

        # Set the sprite's flip_x to False

        sprite.flip_x = False

        # Increment the sprite's center_x by speed
        # ---> TEST AFTER THIS LINE <--- #

        sprite.center_x += speed

    # --- Move up and down --- #

    # If goal_y is less than the sprite's center_y - 10
    # and the sprite's center_y is greater than 120

    if goal_y < sprite.center_y - 10 and sprite.center_y > 120:

        # Decrement the sprite's center_y by speed
        # ---> TEST AFTER THIS LINE <--- #

        sprite.center_y -= speed

    # Else if goal_y is greater than the sprite's
    # center_y + 10

    elif goal_y > sprite.center_y + 10:

        # Increment the sprite's center_y by speed
        # ---> TEST AFTER THIS LINE <--- #

        sprite.center_y += speed

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# --- Setup --- #

# Open a window called w with size 1018 x 573

w = pygame.display.set_mode([1018, 573])

# Create a clock called c

c = pygame.time.Clock()

# --- Sprites --- #

# Create a sprite called background using
# "LivingRoom.jpg" at position 0, 0

background = tsk.Sprite("LivingRoom.jpg", 0, 0)

# Create a sprite called ball using "TennisBall.png" at
# position 0, 0

ball = tsk.Sprite("TennisBall.png", 0, 0)

# Create a sprite called pug using "Pug.png" at
# position 500, 200

pug = tsk.Sprite("Pug.png", 500, 200)

#### ---- MAIN LOOP ---- ####

# Create a variable drawing and set it to True

drawing = True

# Loop while drawing

while drawing:

    # --- Event loop --- #

    # Start an event loop

    for event in pygame.event.get():

        # Check if the event type is QUIT

        if event.type == pygame.QUIT:

            # Set drawing to False
            # ---> TEST AFTER THIS LINE <--- #

            drawing = False

    ##### ---- MOVE ---- ####

    # --- Tennis ball follows mouse --- #

    # Set the ball's center to the mouse's get_pos
    # ---> TEST AFTER THIS LINE <--- #

    ball.center = pygame.mouse.get_pos()


    # --- Pug follows ball --- #

    # Set speed to .05 * c.get_time()

    speed = 0.05 * c.get_time()
    
    # CALL move_towards with ARGUMENTS pug, the ball's
    # center, and speed

    move_towards(pug, ball.center, speed)


    #### ---- DRAW ---- ####

    # Draw the background

    background.draw()

    # Draw the pug

    pug.draw()

    # Draw the ball

    ball.draw()

    # --- Finish --- #

    # Flip the display

    pygame.display.flip()

    # Tick c with framerate 30
    # ---> TEST AFTER THIS LINE <--- #

    c.tick(30)

# Turn in your Coding Exercise.
