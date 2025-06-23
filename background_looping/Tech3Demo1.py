"""
LESSON: 5.1 - Sprites
TECHNIQUE 3: Background Looping
DEMO 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

background = tsk.Sprite("SpringMountains.png", 0, 0)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.center_x -= 8
    if background.center_x < 0:
        background.center_x = 1018


    background.draw()
    pygame.display.flip()