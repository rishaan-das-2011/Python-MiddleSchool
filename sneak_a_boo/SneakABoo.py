"""
LESSON: 6.2 - Return Values
EXERCISE: Sneak-A-Boo
"""

#### ---- LIBRARIES ---- ####

# Import the tsk library

import tsk

# Import the random library

import random

# Import pygame

import pygame

# Initialize pygame

pygame.init()


#### ----------------------------------- ####
#### ---- GET NEW LOCATION FUNCTION ---- ####
#### ----------------------------------- ####

# DEFINE the function get_new_location with PARAMETERS
# center and speed
def get_new_location(center, speed):

    # Assign x, y the value center
    x, y = center

    # If is_key_down with the K_LEFT key is True
    if tsk.is_key_down(pygame.K_LEFT):

        # Decrement x by speed
        x -= speed

    # If is_key_down with the K_RIGHT key is True
    if tsk.is_key_down(pygame.K_RIGHT):

        # Increment x by speed
        x += speed

    # If is_key_down with the K_UP key is True
    if tsk.is_key_down(pygame.K_UP):
   
        # Decrement y by speed
        y -= speed

    # If is_key_down with the K_DOWN key is True
    if tsk.is_key_down(pygame.K_DOWN):

        # Increment y by speed
        y += speed

    # RETURN a tuple with x and y
    # ---> TEST AFTER THIS LINE <--- #
    return (x, y)


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# --- Setup --- #

# Create a 1018 x 573 window and store it in variable w
w = pygame.display.set_mode([1018, 573])

# Create a clock and store it in variable c
c = pygame.time.Clock()


# --- Sprites --- #

# Assign background a new Sprite using LivingRoom.jpg
# at 0, 0
bg = tsk.Sprite("LivingRoom.jpg", 0, 0)

# Assign reader a new Sprite using PersonReading.png
# at a random x between 200 and 800 and a random y
# between 0 and 300
reader = tsk.Sprite("PersonReading.png", random.randint(200, 800), random.randint(0, 300))

# Assign ghost a new Sprite using Ghost.png at 0, 0
ghost = tsk.Sprite("Ghost.png", 0, 0)


# --- Variables --- #

# Assign timer the value 4500
timer = 4500

# Assign timer_bar a Rect at 0, 0 with width 20 and
# height 600
timer_bar = pygame.Rect(0, 0, 20, 600)

# Assign frame_count the value 0
frame_count = 0



#### ---- MAIN LOOP ---- ####

# Create a variable called drawing that starts as True
drawing = True

# Loop while drawing
while drawing:


    # --- Event Loop --- #

    # Start an event loop
    for event in pygame.event.get():

        # If the event type is QUIT
        if event.type == pygame.QUIT:

            # Set drawing to False
            # ---> TEST AFTER THIS LINE <--- #
            drawing = False


    # --- Calculate new ghost position --- #

    # If timer is more than 0
    if timer > 0:

        # Set speed to .2 multiplied by c.get_time()
        speed = 0.2 * c.get_time()

        # Set ghost.center to the result of CALLing
        # get_new_location with ghost.center and speed
        ghost.center = get_new_location(ghost.center, speed)


    # --- Move the timer bar down --- #

    # Increment the timer_bar's y by the int typecast
    # of .15 * c.get_time()
    timer_bar.y += int(0.15 * c.get_time())

    # Increment frame_count by 1
    frame_count += 1


    # --- If time is up, reader may be startled --- #

    # If timer is 0 or less and the ghost and reader
    # sprites are colliding
    if timer <= 0 and pygame.sprite.collide_rect(ghost, reader):

        # Set the reader's image to "PersonStartled.png"
        # ---> TEST AFTER THIS LINE <--- #
        reader.image = "PersonStartled.png"


    # --- Draw scene --- #

    # Draw the background
    bg.draw()

    # Draw the timer_bar rect with window w and green
    pygame.draw.rect(w, (0, 255, 0), timer_bar)

    # If the frame_count mod 10 is 0
    if frame_count % 10 == 0:

        # Draw a white circle with window w, at the
        # ghost's center_x and center_y (typecast to
        # ints) with radius 10
        pygame.draw.circle(w, (255, 255, 255), ghost.center, 10)

    # Draw the reader
    reader.draw()

    # If timer is 0 or less
    if timer <= 0:

        # Draw the ghost
        ghost.draw()


    # --- Finish --- #

    # Decrement timer by c.get_time()
    timer -= c.get_time()

    # Flip the display
    pygame.display.flip()

    # Tick clock c with framerate 30
    # ---> TEST AFTER THIS LINE <--- #
    c.tick(30)




# Turn in your Coding Exercise.