"""
LESSON: 5.4 - Sprites in Lists
WARMUP 5
"""

import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("FantasyPlains.jpg", 0, 0)

wiz_sheet = tsk.ImageSheet("WizardWalking.png", 4, 6)
drag_sheet = tsk.ImageSheet("DragonFlying.png", 4, 6)

wizard = tsk.Sprite(wiz_sheet, 500, 200)
dragon = tsk.Sprite(drag_sheet, 0, 0)

gems = []

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    dragon.center = pygame.mouse.get_pos()

    # If the dragon and wizard collide, spill a gem

    if pygame.sprite.collide_rect(wizard, dragon):
        gem = tsk.Sprite("RoundGemPink.png", random.randint(450, 700), random.randint(450, 500))
        gems.append(gem)



    wizard.update(c.get_time())
    dragon.update(c.get_time())

    background.draw()
    wizard.draw()
    dragon.draw()

    for gem in gems:
        gem.draw()

    pygame.display.flip()
    c.tick(30)