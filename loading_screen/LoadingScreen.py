"""
LESSON: 4-3
PROJECT: Loading Screen
"""

#### ---- SETUP ---- ####

# --- Pygame window --- #

# Import pygame

import pygame

# Initialize pygame

pygame.init()

# Open a [280, 150] window and assign to window

window = pygame.display.set_mode([280, 150])

# --- Variables --- #

# Create variable light and assign it color tuple
# (200, 200, 255)

light = (200, 200, 255)

# Create variable dark and assign it color tuple
# (100, 100, 255)

dark = (100, 100, 255)

# Create a variable dark_one and assign it 0

dark_one = 0

# --- Create list of circle centers --- #
 
# Create variable margin and assign value 40

margin = 40

# Create an empty list and assign it to centers

centers = []

# FOR i in RANGE 5

for i in range(5):

    # Create variable point and assign it a coordinate
    # tuple with x value margin + i * 50 and y value 75

    point = (margin + i * 50, 75) 

    # Append point to centers
    # ---> TEST AFTER THIS LINE <--- #

    centers.append(point)

#### ---- MAIN LOOP ---- ####

# Create variable drawing and assign value True

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


    #### ---- DRAW CIRCLES ---- ####

    # Fill the window with white
    # ---> TEST AFTER THIS LINE <--- #

    window.fill((255, 255, 255))


    # --- Draw all light circles except 1 dark --- #    

    # FOR i in RANGE LEN of centers

    for i in range(len(centers)):

        # If i is not equal to dark_one

        if i != dark_one:

            # Draw a circle in window with color light,
            # center from centers list at INDEX i, and
            # radius 15
            # ---> TEST AFTER THIS LINE <--- #

            pygame.draw.circle(window, light, centers[i], 15)

        # else

        else:
            
            # Draw a circle in window with color dark,
            # center from centers list at INDEX i, and
            # radius 15
            # ---> TEST AFTER THESE LINES <--- #

            pygame.draw.circle(window, dark, centers[i], 15)

    #### ---- FINISH DRAWING ---- ####

    # --- Change which circle should be dark next --- #

    # Increment dark_one by 1

    dark_one += 1

    # Assign dark_one the value dark_one % LEN of centers
    # variable = variable % len(list)
    # ---> TEST AFTER THIS LINE <--- #

    dark_one = dark_one % len(centers)

    # --- Finish the frame --- #

    # Flip the display

    pygame.display.flip()

    # Wait 300 milliseconds
    # ---> TEST AFTER THIS LINE <--- #

    pygame.time.wait(300)



# Turn in your Coding Exercise.




    
