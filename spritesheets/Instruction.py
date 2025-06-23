"""
LESSON: 5.2 - Sprite Sheet Animation
INSTRUCTION 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Hills.jpg", 0, 0)
run_sheet = tsk.ImageSheet("HedgehogRun.png", 5, 6)
hedgehog = tsk.Sprite(run_sheet, 100, 200)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Make the hedgehog follow the mouse
    x, y = pygame.mouse.get_pos()
    hedgehog.center = (x, y)

    # Draw the background and hedgehog
    background.draw()
    hedgehog.update(c.get_time())
    hedgehog.draw()

    pygame.display.flip()
    c.tick(30)