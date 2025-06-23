"""
LESSON: 5.1 - Sprites
TECHNIQUE 1: Make a Sprite
PRACTICE 2
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

sky = tsk.Sprite("OutdoorEmptySky.png", 0, 0)
panda = tsk.Sprite("PandaPilot.png", 50, 40)


drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False


    sky.draw()
    panda.draw()
    pygame.display.flip()


# Turn in your Coding Exercise.
