"""
LESSON: TechSmart Studio Project
EXERCISE: Rectangles
"""

#### ---- SETUP ---- ####

# --- Libraries --- #

# Import pygame

import pygame

# Initialize pygame

pygame.init()

# --- Variables --- #

# Open a window of size [400, 100] and assign to window

window = pygame.display.set_mode([400, 100])

# Assign variable colors a LIST of 4 COLOR TUPLES with
# the values BLACK, RED, GREEN, and BLUE
# ---> TEST AFTER THIS LINE <--- #

colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Assign x_values a list of four integers: 0, 100, 200,
# and 300

x_values = [0, 100, 200, 300]

#### ---- DRAW LOOP ---- ####

# Create variable drawing and assign the value True

drawing = True

# Loop while drawing

while drawing:

    # --- Event loop --- #

    # Create an event loop that gets all pygame events

    for event in pygame.event.get():
 
        # Check if event type is QUIT

        if event.type == pygame.QUIT:

            # Assign drawing the value False
            # ---> TEST AFTER THIS LINE <--- #

            drawing = False

    # --- Draw rectangles --- #

    # FOR i in RANGE 4

    for i in range(4):

        # Create a rectangle with left value from x_values
        # at INDEX i, top 0, and width and height 100.
        # Assign to variable r

        r = pygame.Rect(x_values[i], 0, 100, 100)

        # Draw the rectangle r in window using the color
        # from colors at INDEX i

        pygame.draw.rect(window, colors[i], r)

    # --- Finish --- #

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #

    pygame.display.flip()



# Turn in your Coding Exercise.
