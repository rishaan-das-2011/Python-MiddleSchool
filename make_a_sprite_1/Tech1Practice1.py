"""
LESSON: 5.1 - Sprites
TECHNIQUE 1: Make a Sprite
PRACTICE 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

bush = tsk.Sprite("OutdoorBushScene.jpg", 0, 0)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False


    bush.draw()

    pygame.display.flip()
# Turn in your Coding Exercise.
