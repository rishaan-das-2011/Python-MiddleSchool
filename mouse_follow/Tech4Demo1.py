"""
LESSON: 5.1 - Sprites
TECHNIQUE 4: Mouse Follow
DEMO 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

background = tsk.Sprite("OutdoorMountainScene.jpg", 0, 0)
pony = tsk.Sprite("Pony.png", 0, 0)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    x, y = pygame.mouse.get_pos()
    pony.center = (x, y)

    background.draw()
    pony.draw()
    pygame.display.flip()