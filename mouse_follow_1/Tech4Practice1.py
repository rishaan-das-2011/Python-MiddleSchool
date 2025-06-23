"""
LESSON: 5.1 - Sprites
TECHNIQUE 4: Mouse Follow
PRACTICE 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

background = tsk.Sprite("OutdoorBushScene.jpg", 0, 0)
beehive = tsk.Sprite("Beehive.png", 140, 0)
bee = tsk.Sprite("Bee.png", 0, 0)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False


    x, y = pygame.mouse.get_pos()
    bee.center = (x, y)


    background.draw()
    bee.draw()
    beehive.draw()
    pygame.display.flip()


# Turn in your Coding Exercise.
