"""
LESSON: 5.1 - Sprites
WARMUP 2
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

# Declare sprites here

Space = tsk.Sprite("Space.jpg", 0, 0)
desert = tsk.Sprite("DesertPlanet.png", 0, 300)
star = tsk.Sprite("ShootingStar.png", 800, 300)


drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Draw sprites here

    Space.draw()
    desert.draw()
    star.draw()
    pygame.display.flip()

