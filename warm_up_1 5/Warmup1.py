"""
LESSON: 5.4 - Sprites in Lists
WARMUP 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("SkyMountains.jpg", 0, 0)
puffin_sheet = tsk.ImageSheet("Puffin_Fly.png", 5, 6)
puffin = tsk.Sprite(puffin_sheet, 0, 200)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # Check for mouse down and reset puffin here

        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and puffin.rect.collidepoint(x, y):
            puffin.center_x = 0


    background.draw()

    puffin.center_x += 0.2 * c.get_time()
    puffin.update(c.get_time())
    puffin.draw()
    pygame.display.flip()

    c.tick(30)