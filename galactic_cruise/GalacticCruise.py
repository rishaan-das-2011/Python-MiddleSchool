# — Libraries — #
import tsk
import pygame

# Initialize pygame
pygame.init()

# — Drawing variables — #
window = pygame.display.set_mode([1018, 573])
space = tsk.Sprite("space_background.jpg", 0, 0)
galaxy = tsk.Sprite("galaxies_scrolling.png", 0, 0)
stars = tsk.Sprite("stars_scrolling.png", 0, 0)
asteroids = tsk.Sprite("asteroids_scrolling.png", 0, 0)

# Scrolling speeds
galaxies_speed = -1
stars_speed = -2
asteroids_speed = -7

# Image widths
GALAXY_WIDTH = 1900
STARS_WIDTH = 3025
ASTEROIDS_WIDTH = 2400

# — Loop variables — #
drawing = True

#### ---- MAIN LOOP ---- ####
while drawing:
    # — Event loop — #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # — Scroll elements — #
    
    galaxy.x += galaxies_speed
    stars.x += stars_speed
    asteroids.x += asteroids_speed

    # Reset positions when fully off-screen
    
    if galaxy.x <= -GALAXY_WIDTH:
        galaxy.x = 0
    if stars.x <= -STARS_WIDTH:
        stars.x = 0
    if asteroids.x <= -ASTEROIDS_WIDTH:
        asteroids.x = 0

    #### ---- DRAW OUTPUT ---- ####
    space.draw()
    stars.draw()
    galaxy.draw()
    
    asteroids.draw()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pygame.display.flip()# Turn in your Coding# Import the tsk library# Import the pygame library# Initialize pygame# Open a new window of size [1018, 573] and assign to
# window# Create a new SPRITE object for the space background
# using the "space_background.jpg" image at (0, 0)# Create a new SPRITE object for the galaxies using
# the "galaxies_scrolling.png" image at (0, 0)# Create a new SPRITE object for the stars using
# the "stars_scrolling.png" image at (0, 0)# Create a new SPRITE object for the asteroids using
# the "asteroids_scrolling.png" image at (0, 0)# Create a variable for galaxies_speed, set to -1# Create a variable for stars_speed, set to -2# Create a variable for asteroids_speed, set to -7# Create a variable called drawing and assign it True# Loop while drawing    # Create an event loop        #  If the event is equal to the QUIT event            # Set drawing to False    # If the galaxies sprite's CENTER_X is less than 0        # Set the galaxies sprite's CENTER_X to 1900    # Increment CENTER_X of galaxies
    # by galaxies_speed
    # ---> TEST AFTER THIS LINE <--- #    # If the stars sprite's CENTER_X is less than 0        # Set the stars' CENTER_X to 3025    # Increment CENTER_X of stars
    # by stars_speed
    # ---> TEST AFTER THIS LINE <--- #    # If the asteroids sprite's CENTER_X is less than 0        # Set asteroids' CENTER_X to 2400    # Increment CENTER_X of asteroids
    # by asteroids_speed
    # ---> TEST AFTER THIS LINE <--- #    # DRAW the space background    # DRAW the stars    # DRAW the galaxies    # DRAW the asteroids    # Flip the display
    # ---> TEST AFTER THIS LINE <--- #