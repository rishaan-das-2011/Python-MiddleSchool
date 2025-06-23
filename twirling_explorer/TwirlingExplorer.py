"""
LESSON: 5.2 - Spritesheets
EXERCISE: Twirling Explorer
"""

#### ---- SET UP ---- ####

# --- Libraries ---  #

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

# Create a new Clock and assign to c

c = pygame.time.Clock()

# Create a SPRITE object called background using the
# "AlienSpace.jpg" image at 0, 0

background = tsk.Sprite("AlienSpace.jpg", 0, 0)

# Create an IMAGESHEET called ship_sheet using the
# "RoundShipSpin.png" image with 5 rows and 3 columns

ship_sheet = tsk.ImageSheet("RoundShipSpin.png", 5, 3)

# Create a new SPRITE object called ship using
# ship_sheet, positioned at 100, 100

ship = tsk.Sprite(ship_sheet, 100, 100)

# Create a new variable movement_speed, set to 0.3

movement_speed = 0.3

# Set the ship's IMAGE_ANIMATION_RATE to 30

image_animation_rate = 30

# Create a new boolean called ship_moving_right,
# set to True

ship_moving_right = True

# Create a new boolean called ship_moving_down,
# set to True

ship_moving_down = True

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


        # --- Keyboard input --- #

        # Else if event.type is KEYDOWN and the
        # event.key is K_DOWN

        elif event.type == pygame.KEYDOWN and tsk.get_key_pressed(pygame.K_DOWN):

            # If the ship's IMAGE_ANIMATION_RATE
            # is greater than 0

            if ship.image_animation_rate > 0:

                # Decrement movement_speed by 0.05

                movement_speed -= 0.95

                # Decrement ship's
                # IMAGE_ANIMATION_RATE by 5

                ship.image_animation_rate -= 5

        # Else if event.type is KEYDOWN and the
        # event.key is K_UP

        elif event.type == pygame.KEYDOWN and 

            # If the ship's IMAGE_ANIMATION_RATE
            # is less than 50


                # Increment movement_speed by 0.05


                # Increment ship's
                # IMAGE_ANIMATION_RATE by 5
                # ---> TEST AFTER THIS LINE <--- #



    # --- Check walls --- #

    # Store the ship's CENTER in variables x and y


    # If the ship's x is less than 0


        # Set ship_moving_right to True


    # If the ship's x is greater than 1018


        # Set ship_moving_right to False


    # If the ship's y is less than 0


        # Set ship_moving_down to True


    # If the ship's y is greater than 573


        # Set ship_moving_down to False



    # --- Move ship --- #

    # If the ship is moving_right


        # Increment x by movement_speed
        # multiplied by c.get_time()


    # Else


        # Decrement x by movement_speed
        # multiplied by c.get_time()


    # If the ship is moving_down


        # Increment its y by movement_speed
        # multiplied by c.get_time()


    # Else


        # Decrement its y by movement_speed
        # multiplied by c.get_time()


    # Set the ship's CENTER back to (x, y)
    # ---> TEST AFTER THIS LINE <--- #



    # --- Animate and draw --- #

    # UPDATE the ship's animation with c.get_time()


    # DRAW the background


    # DRAW the ship


    # Flip the display


    # Tick c at framerate 30
    # ---> TEST AFTER THIS LINE <--- #

    
    

# Turn in your Coding Exercise.
