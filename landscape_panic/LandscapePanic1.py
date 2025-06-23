"""
LESSON: 5.1 - Sprites
EXERCISE: Landscape Panic
PROBLEM: 1 of 3
"""

#### ---- SET UP ---- ####

# Import libraries, and initialize pygame
import tsk
import pygame
pygame.init()

# Create a new WINDOW
window = pygame.display.set_mode([1018, 573])

# Create the sprites
sky = tsk.Sprite("outdoor_sky.png", 0, 0)
back_mountains = tsk.Sprite("outdoor_mountain_b.png", 0, 0)
front_mountains = tsk.Sprite("outdoor_mountain_a.png", 0, 0)
foreground = tsk.Sprite("outdoor_foreground.png", 0, 0)

# Initialize drawing variable to True so the main loop runs
drawing = True

#### ---- MAIN LOOP ---- ####

while drawing:
    # — Event Loop — #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # — Draw the scene — #
    
    sky.draw()        
    back_mountains.draw()  
    front_mountains.draw() 
    foreground.draw()    
    pygame.display.flip() 