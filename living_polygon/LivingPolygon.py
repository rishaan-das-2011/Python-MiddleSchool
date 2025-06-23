"""
LESSON: 4.1 - Lists
EXERCISE: Living Polygon
"""

#### ---- SET UP ---- ####

# --- Pygame --- #

# Import pygame

import pygame

# Initialize pygame

pygame.init()

# --- Window --- #

# Open a [400, 400] window and assign it to window

window = pygame.display.set_mode((400, 400))

# Fill window with white
# ---> TEST AFTER THIS LINE <--- #

window.fill((255, 255, 255))


# --- Starting points --- #

# Create a LIST containing three point tuples:
# (200, 25), (300, 25), and (300, 50), and assign to
# the variable points
# ---> TEST AFTER THIS LINE <--- #

points = [(200, 25), (300, 25), (300, 50)]

#### ---- MAIN LOOP ---- ####

# Create variable drawing and assign it True

drawing = True

# Loop while drawing

while drawing:

    # --- Event loop --- #

    # Create an event loop that checks all events

    for event in pygame.event.get():

        # IF the event type is QUIT

        if event.type == pygame.QUIT:

            # Assign drawing the value False
            # ---> TEST AFTER THIS LINE <--- #

            drawing = False


    # --- Draw frame --- #

    # Fill window with white

    window.fill((255, 255, 255))

    # Draw a polygon in window with any color using the
    # list points

    pygame.draw.polygon(window, (255, 0, 0), points)

    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #

    pygame.display.flip()

    # --- Get input --- #

    # Get input asking for an x coordinate and assign
    # to variable x

    x = input("Enter an x coordinate (or type quit): ")

    # If x is equal to "quit"

    if x == "quit":

        # break
        break

    # Get input asking for a y coordinate and assign to
    # variable y

    y = input("Enter a y coordinate (or type quit): ")

    # If y is equal to "quit"

    if y == "quit":

        # break
        # ---> TEST AFTER THIS LINE <--- #
    
        break    

    # --- Change polygon --- #

    # Create a point tuple with x and y typecasted to
    # an int and assign it to new_point
    new_point = (int(x), int(y))

    # APPEND new_point to the list points
    # list.append(value)

    points.append(new_point)

    # --- Output current points --- #

    # Print "This is the polygon: " + points typecasted
    # to a string

    print("This is the polygon: " + str(points))

    # Print a blank line
    # ---> TEST AFTER THIS LINE <--- #
print() 



# Turn in your Coding Exercise.

