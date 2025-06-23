"""
LESSON: 5.1 - Sprites
TECHNIQUE 3: Background Looping
PRACTICE 2
"""

import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

space1 = tsk.Sprite("Space.jpg", 0, 0)
space2 = tsk.Sprite("Space.jpg", 1018, 0)
asteroids1 = tsk.Sprite("AsteroidsScrolling.png", 0, 150)
asteroids2 = tsk.Sprite("AsteroidsScrolling.png", 1018, 150)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    space1.center_x -= 5
    space2.center_x -= 5
    asteroids1.center_x -= 5
    asteroids2.center_x -= 5


    if space1.center_x <= -509: 
        space1.center_x = space2.center_x + 1018
    if space2.center_x <= -509:
        space2.center_x = space1.center_x + 1018
        
    if asteroids1.center_x <= -509:
        asteroids1.center_x = asteroids2.center_x + 1018
    if asteroids2.center_x <= -509:
        asteroids2.center_x = asteroids1.center_x + 1018

    space1.draw()
    space2.draw()
    asteroids1.draw()
    asteroids2.draw()
    
    pygame.display.flip()


# Turn in your Coding Exercise.
