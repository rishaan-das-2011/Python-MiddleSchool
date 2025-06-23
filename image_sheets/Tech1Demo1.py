"""
LESSON: 5.2 - Spritesheet Animation
TECHNIQUE 1: Image Sheets in Sprites
DEMO 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("SkyMountains.jpg", 0, 0)


puffin_sheet = tsk.ImageSheet("Puffin_Fly.png", 5, 6)
puffin = tsk.Sprite(puffin_sheet, 475, 400)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.draw()
    puffin.update(c.get_time())
    puffin.draw()


    pygame.display.flip()
    c.tick(30)