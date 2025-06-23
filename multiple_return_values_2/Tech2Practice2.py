"""
LESSON: 6.2 - Return Values
TECHNIQUE 2: Multiple Return Values
PRACTICE 2
"""

#### ---- LIBRARIES ---- ####
import random
import pygame
pygame.init()


#### ------------------------------ ####
#### ---- GET CENTERS FUNCTION ---- ####
#### ------------------------------ ####
def get_centers():

    x = 100
    y = 100

    # Create an empty list
    
    centers = []

    for i in range(10):

        # Create a point tuple and append it to the
        # list

        centers.append((x, y))

        # Move the next point
        x += random.randint(0, 150)
        y += random.randint(0, 50)

        if x > 1000:
            x = 1000
        if y > 550:
            y = 550

    # Return the list

    return centers

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# Setup
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Call the function and save the resulting list

centers = get_centers()

circles_drawn = 0
timer = 0


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Time
    if timer >= 1000:
        timer = 0
        circles_drawn += 1

    # Draw
    w.fill((255, 255, 255))
    for i in range(circles_drawn):
        if i >= 10:
            drawing = False
            break

        # Draw the next circle using the center at
        # index i in the list you created

        pygame.draw.circle(w, (0, 0, 0), centers[i], 20, 2)

    # Finish
    pygame.display.flip()
    c.tick(30)
    timer += c.get_time()


# Turn in your Coding Exercise.
