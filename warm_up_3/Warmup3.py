"""
LESSON: 5.1 - Sprites
WARMUP 3
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
sky = tsk.Sprite("SkyMountains.jpg", 0, 0)
puffin = tsk.Sprite("PuffinFly.png", 0, 300)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Move and scale puffin here

    puffin.center_x += 7
    puffin.center_y -= 7
    puffin.scale -= 0.02



    if puffin.scale < 0.1:
        drawing = False

    sky.draw()
    puffin.draw()
    pygame.display.flip()

    pygame.time.wait(50)