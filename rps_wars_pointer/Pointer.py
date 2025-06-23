"""
LESSON: RPS Wars Project
EXERCISE: Pointer
"""

#### ---- LIBRARIES ---- ####

# Import pygame

import pygame

# Initialize pygame

pygame.init()

#### ----------------------------- ####
#### ---- DRAW ARROW FUNCTION ---- ####
#### ----------------------------- ####

# DEFINE the function draw_arrow with PARAMETERS
# window, point, color, and up

def draw_arrow(window, point, color, up):

    # --- Calculate points --- #

    # Assign x, y the value point

    (x, y) = point

    # If up

    if up:

        # Assign mid the value y + 65

        mid = y - 65

        # Assign base_y the value mid

        base_y = mid - 45

    # Otherwise

    else:

        # Assign mid the value y - 65

        mid = y + 65

        # Assign base_y the value y - 110

        base_y = mid

    # Assign head_left the value x - 30

    head_left = x - 30

    # Assign head_right the value x + 30

    head_right = x + 30

    # Assign base_left the value x - 10

    base_left = x - 10

    # --- Draw shapes --- #

    # Draw a polygon with window and color connecting
    # points (x, y), (head_left, mid), (head_right, mid)

    pygame.draw.polygon(window, color, [(x, y), (head_left, mid), (head_right, mid)])

    # Create a Rect called base at base_left, base_y,
    # with width 20 and height 45

    base = pygame.Rect(base_left, base_y, 20, 45)

    # Draw the base rect in window with color
    # ---> TEST AFTER THIS LINE <--- #

    pygame.draw.rect(window, color, base)


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# Set w to a new 500 x 500 window

w = pygame.display.set_mode([500, 500])

# Set up_arrow to True

up_arrow = True

#### ---- MAIN LOOP ---- ####

# Set drawing to True

drawing = True

# Loop while drawing

while drawing:

    # --- Event loop --- #

    # Create an event loop

    for event in pygame.event.get():

        # If the event type is QUIT

        if event.type == pygame.QUIT:

            # Set drawing to False

            drawing = False

        # Else if the event type is MOUSEBUTTONDOWN

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Set up_arrow to not up_arrow

            up_arrow = not up_arrow

    # --- Draw arrow --- #

    # Set mouse to the mouse position

    mouse = pygame.mouse.get_pos()

    # Fill the window with white

    w.fill((255, 255, 255))

    # CALL draw_arrow with w, mouse, the color of your
    # choice, and up_arrow

    draw_arrow(w, mouse, (250, 150, 200), up_arrow)

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #

    pygame.display.flip()



# Turn in your Coding Exercise.
