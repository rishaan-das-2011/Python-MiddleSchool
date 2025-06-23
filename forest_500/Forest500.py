"""
LESSON: 6.3 - Complex Parameters
EXERCISE: Forest 500
"""

#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()


#### -------------------------------- ####
#### ---- MOVE HEDGEHOG FUNCTION ---- ####
#### -------------------------------- ####

# DEFINE the move_hedgehog function with PARAMETERS
# sprite, goal, and speed

def move_hedgehog(sprite, goal, speed):

    # If sprite's center_y is less than goal - 10

    if sprite.center_y < goal - 10:

        # Increment sprite's center_y by speed
        # ---> TEST AFTER THIS LINE <--- #

        sprite.center_y += speed

    # If sprite's center_y is greater than goal + 10
    # and sprite's center_y is greater than 250

    if sprite.center_y > goal + 10 and sprite.center_y > 250:

        # Decrement sprite's center_y by speed
        # ---> TEST AFTER THIS LINE <--- #

        sprite.center_y -= speed

#### ------------------------------- ####
#### ---- SPAWN SPRITE FUNCTION ---- ####
#### ------------------------------- ####

# DEFINE the function spawn_sprite with PARAMETER
# sprite_list

def spawn_sprite(sprite_list):

    # Create a list called obstacles with strings
    # "Bush.png", "DarkRock.png", "LightRock.png" and
    # "Bee.png"

    obstacles = ["Bush.png", "DarkRock.png", "LightRock.png", "Bee.png"]

    # Create a Sprite called new_sprite with a random
    # CHOICE from obstacles and position 1020 for x
    # and a random y between 250 and 450

    new_sprite = tsk.Sprite(random.choice(obstacles), 1020, random.randint(250, 450))
    
    # Append new_sprite to sprite_list
    # ---> TEST AFTER THIS LINE <--- #

    sprite_list.append(new_sprite)

#### ----------------------------------- ####
#### ---- CHECK COLLISIONS FUNCTION ---- ####
#### ----------------------------------- ####

# DEFINE the check_collisions function with PARAMETERS
# sprite and sprite_list

def check_collisions(sprite, sprite_list):

    # Assign hit_objects an empty list

    hit_objects = []
    
    # For each item in sprite_list

    for item in sprite_list:

        # If item and sprite rectangles collide

        if pygame.sprite.collide_rect(item, sprite):

            # Append item to hit_objects

            hit_objects.append(item)

    # For each item in hit_objects

    for item in hit_objects:

        # Remove item from sprite_list

        sprite_list.remove(item)

    # RETURN the length of hit_objects list
    # ---> TEST AFTER THIS LINE <--- #

    return len(hit_objects)

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

#### ---- SETUP ---- ####
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# --- Sprites --- #

# Create a Sprite called back at 0, 0 with image
# "ForestScrolling.jpg"

back = tsk.Sprite("ForestScrolling.jpg", 0, 0)

# Create an ImageSheet called run using
# "HedgehogRun.png" with 5 rows and 6 columns

run = tsk.ImageSheet("HedgehogRun.png", 5, 6)

# Create a Sprite called hedgehog using run at position
# -75, 350

hedgehog = tsk.Sprite(run, -75, 350)

# Set hedgehog's scale to .5
# ---> TEST AFTER THIS LINE <--- #

hedgehog.scale = 0.5

# --- Obstacle variables --- #

# Create an empty list called obstacles

obstacles = []

# Assign collisions the value 0

collisions = 0

# Assign spawn_timer the value 0

spawn_timer = 0

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    #### ---- MOVE ---- ####

    # --- Background --- #

    # Decrement back's center_x by .2 * c.get_time()

    back.center_x -= 0.2 * c.get_time()

    # If back's center_x is less than or equal to 0

    if back.center_x <= 0:

        # Set back's center_x to 1018
        # ---> TEST AFTER THIS LINE <--- #

        back.center_x = 1018

    # --- Hedgehog --- #

    # Assign x, y the mouse position

    x, y = pygame.mouse.get_pos()

    # CALL the move_hedgehog function with ARGUMENTS
    # hedgehog, y, and .2 * c.get_time()

    move_hedgehog(hedgehog, y, 0.2 * c.get_time())

    # --- Obstacles --- #

    # For each sprite in obstacles

    for sprite in obstacles:

        # Decrement sprite's x by .2 * c.get_time()
        # ---> TEST AFTER THIS LINE <--- #

        sprite.x -= 0.2 * c.get_time()

    #### ---- ADD & REMOVE ---- ####

    # --- Spawn new sprites --- #

    # If spawn_timer is greater than 4000

    if spawn_timer > 4000:

        # CALL spawn_sprite with ARGUMENT obstacles

        spawn_sprite(obstacles)
    
        # Set spawn_timer to 0
        # ---> TEST AFTER THIS LINE <--- #

        spawn_timer = 0

    # --- Check for collisions --- #

    # Increment collisions by the result of CALLing
    # check_collisions with ARGUMENTS hedgehog and
    # obstacles

    collisions += check_collisions(hedgehog, obstacles)

    # If collisions is greater than or equal to 5

    if collisions >= 5:

        # Set drawing to False
        # ---> TEST AFTER THIS LINE <--- #

        drawing = False

    #### ---- DRAW ---- ####

    # --- Draw sprites --- #

    # Draw back

    back.draw()

    # Draw hedgehog

    hedgehog.draw()

    # Update hedgehog with c.get_time()

    hedgehog.update(c.get_time())

    # For each sprite in obstacles

    for sprite in obstacles:

        # Draw sprite

        sprite.draw()

    # --- Finish --- #
    pygame.display.flip()
    c.tick(30)

    # Increment spawn_timer by c.get_time()
    # ---> TEST AFTER THIS LINE <--- #

    spawn_timer += c.get_time()



# Turn in your Coding Exercise.
