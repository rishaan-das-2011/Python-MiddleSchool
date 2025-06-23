"""
LESSON: 5.3 - Sprite Collision
EXERCISE: Pug vs Dragon
"""

#### ---- SET UP ---- ####

# --- Libraries ---  #

# Import the tsk library

import tsk

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

# Create a new SPRITE called background using the
# "FantasyPlains.jpg" image at (0, 0)

background = tsk.Sprite("FantasyPlains.jpg", 0, 0)

# Create a new SPRITE called pug using the "Pug.png"
# image at (300, 300)

pug = tsk.Sprite("Pug.png", 300, 300)

# Create an IMAGESHEET called dragon_sheet using
# "DragonFlying.png" with 4 rows and 6 columns

dragon_sheet = tsk.ImageSheet("DragonFlying.png", 4, 6)

# Create a new SPRITE called dragon using dragon_sheet
# at (700, 300)

dragon = tsk.Sprite(dragon_sheet, 700, 300)

# Create a new variable called time, set to 0

time = 0

# Create a new variable called speed, set to 0.1

speed = 0.1

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

    # Get the position of the mouse and assign it
    # to pug_x, pug_y

    pug_x, pug_y = pygame.mouse.get_pos()

    # Set the pug's CENTER to pug_x, pug_y
    # ---> TEST AFTER THIS LINE <--- #

    pug.center = (pug_x, pug_y)

    # --- Move dragon --- #

    # If the dragon's center_x is less than pug_x - 15

    if dragon.center_x < pug_x - 15:

        # Increment the dragon's center_x by speed *
        # c.get_time()

        dragon.center_x += speed * c.get_time()

        # Set the dragon's FLIP_X to False

        dragon.flip_x = False

    # Otherwise if the dragon's center_x is greater
    # than pug_x + 15

    elif dragon.center_x > pug_x + 15:

        # Decrement the dragon's center_x by speed *
        # c.get_time()

        dragon.center_x -= speed * c.get_time()

        # Set the dragon's FLIP_X to True
        # ---> TEST AFTER THIS LINE <--- #

        dragon.flip_x = True

    # If the dragon's center_y is less than pug_y - 15

    if dragon.center_y < pug_y - 15:

        # Increment the dragon's center_y by speed *
        # c.get_time()

        dragon.center_y += speed * c.get_time()

    # Otherwise if the dragon's center_y is greater
    # than pug_y + 15

    elif dragon.center_y > pug_y + 15:

        # Decrement the dragon's center_y by speed *
        # c.get_time()
        # ---> TEST AFTER THIS LINE <--- #

        dragon.center_y -= speed * c.get_time()

    # --- Check for collision --- #

    # If pug and dragon collide with COLLIDE_RECT

    if pygame.sprite.collide_rect(pug, dragon):

        # Set drawing to False
        # ---> TEST AFTER THIS LINE <--- #

        drawing = False


    # --- Update score and difficulty --- #

    # Increment time by get_time

    time += c.get_time()

    # Increment speed by c.get_time() / 200000
    # ---> TEST AFTER THIS LINE <--- #

    speed += c.get_time() / 200000    

    # --- Draw --- #

    # UPDATE the dragon with c.get_time()

    dragon.update(c.get_time())

    # DRAW the background

    background.draw()

    # DRAW the dragon

    dragon.draw()

    # DRAW the pug

    pug.draw()

    # Flip the display

    pygame.display.flip()

    # Tick c by 30
    # ---> TEST AFTER THIS LINE <--- #

    c.tick(30)

#### ---- FINAL SCORE---- ####

# Print time / 1000 converted to a string to tell the
# player how long they lasted
# ---> TEST AFTER THIS LINE <--- #


print("You lasted " + str(time/1000)+ " seconds! ")

# Turn in your Coding Exercise.