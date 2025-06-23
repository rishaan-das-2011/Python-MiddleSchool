"""
LESSON: 5.1 - Sprites
EXERCISE: Human Haircut
"""

#### ---- SET UP ---- ####

# --- Libraries --- #

# Import the tsk library

import tsk

# Import the pygame library

import pygame

# Initialize pygame

pygame.init()

# Create a pygame clock and assign it to c

c = pygame.time.Clock()

# --- Drawing background and face --- #

# Open a new window of size [1018, 573] and assign to
# window

window = pygame.display.set_mode([1018, 573])

# Fill the window with white

window.fill((255, 255, 255))


# Create a new SPRITE object for the robot using the
# "robot_bust.png" image at (0, 0)

robot = tsk.Sprite("robot_bust.png", 0, 0)

# DRAW the robot sprite
# ---> TEST AFTER THIS LINE <--- #

robot.draw()

# --- Animation variables --- #

# Create a variable called hair_color, and assign it
# the value for black (0, 0 ,0)

hair_color = (0, 0, 0)

# Create a variable called drawing and assign it False

drawing = False

# --- Loop variables --- #

# Create a variable called done and assign it False

done = False

#### ---- MAIN LOOP ---- ####

# Loop while not done

while not done:

    # --- Event loop --- #

    # Create an event loop

    for event in pygame.event.get():

        # If the event is equal to the QUIT event

        if event.type == pygame.QUIT:

            # Set done to True
            # ---> TEST AFTER THIS LINE <--- #

            done = True

        # --- Click handling ---- #

        # Elif the event type is MOUSEBUTTONDOWN

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Set drawing to True

            drawing = True

        # Elif the event type is MOUSEBUTTONUP

        elif event.type == pygame.MOUSEBUTTONUP:

            # Set drawing to False
            # ---> TEST AFTER THIS LINE <--- #

            drawing = False

    # --- Drawing with mouse --- #

    # Get the position of the mouse and store it
    # in the variables x, y

    x, y = pygame.mouse.get_pos()

    # If drawing

    if drawing:

        # Draw a circle in the window with hair_color,
        # center (x, y) and radius 10
        # ---> TEST AFTER THIS LINE <--- #

        pygame.draw.circle(window, hair_color, (x, y), 10)

    # Tick clock c with framerate 30

    c.tick(30)

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #

    pygame.display.flip()
    
    
# Turn in your Coding Exercise.    