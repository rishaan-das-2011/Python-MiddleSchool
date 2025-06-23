"""
LESSON: 5.4 - Sprites in Lists
EXERCISE: Beyond the End Zone
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

# Open a new window of size [1018, 573] called window

window = pygame.display.set_mode([1018, 573])

# Create a new Clock called c

c = pygame.time.Clock()

# Create a SPRITE called background using
# "ForestScrolling.jpg" at (0, 0)

background = tsk.Sprite("ForestScrolling.jpg", 0, 0)

# Create a SPRITE called runner using
# "FootballRunner.png" at (400, 225)

runner = tsk.Sprite("FootballRunner.png", 400, 225)

# Create a list called object_names containing:
# "FootballBlocker.png", "Bush.png", "Flower.png",
# "Mole.png", and "Rabbit.png"

object_names = ["FootballBlocker.png", "Bush.png", "Flower.png", "Mole.png", "Rabbit.png"]

# Create an empty list called objects

objects = []

# Create a variable object_spawn_time, set to 2500

object_spawn_time = 2500

# Create a variable timer, set to 0

timer = 0

# Create a variable scroll_speed, set to .25

scroll_speed = 0.25

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

    # --- Spawn objects --- #

    # Increment the timer by c.get_time()

    timer += c.get_time()

    # If the timer is greater than object_spawn_time

    if timer > object_spawn_time:

        # Reset the timer to 0

        timer = 0

        # Create variable new_object_index set to a
        # random integer between 0 and the length of
        # object_names - 1

        new_object_index = random.randint(0, len(object_names) - 1)

        # Create a variable new_object_name set to the
        # item from object_names at new_object_index

        new_object_name = object_names[new_object_index]

        # Create a SPRITE called new_object using
        # new_object_name at (1018, 380)

        new_object = tsk.Sprite(new_object_name, 1018, 380)

        # Append new_object to the objects list
        # ---> TEST AFTER THIS LINE <--- #

        objects.append(new_object)

    # --- Scroll background and objects --- #

    # Decrement the background's center_x by
    # scroll_speed * c.get_time()

    background.center_x -= scroll_speed * c.get_time()

    # If the background's center_x is less than 0

    if background.center_x < 0:

        # Set the center_x of the background to 1018
        # ---> TEST AFTER THIS LINE <--- #

        background.center_x = 1018

    # Create an empty list called objects_to_remove

    objects_to_remove = []
    
    # For every item in the list of objects

    for item in objects:

        # Decrement item's center_x by scroll_speed
        # * c.get_time()

        item.center_x -= scroll_speed * c.get_time()

        # If the item's center_x is less than -100

        if item.center_x < -100:

            # Append the item to objects_to_remove

            objects_to_remove.append(item)

    # For every item in objects_to_remove

    for item in objects_to_remove:

            # Remove item from the objects list
            # ---> TEST AFTER THIS LINE <--- #

            objects_to_remove.remove(item)

    # --- Draw --- #

    # DRAW the background

    background.draw()

    # DRAW the runner

    runner.draw()

    # For each item in objects

    for item in objects:

        # DRAW that sprite

        item.draw()

    # Flip the display

    pygame.display.flip()
    
    # Tick c at 30 framerate
    # ---> TEST AFTER THIS LINE <--- #

    c.tick(30)

# Turn in your Coding Exercise.
