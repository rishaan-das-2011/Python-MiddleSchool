"""
LESSON: 5.2 - Spritesheets
WARMUP 5
"""

import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("FantasyPlains.jpg", 0, 0)
gem = tsk.Sprite("RoundGemPink.png", 500, 300)

sheet = tsk.ImageSheet("WizardWalking.png", 4, 6)
wiz1 = tsk.Sprite(sheet, 0, 150)
wiz2 = tsk.Sprite(sheet, 700, 150)
wiz2.flip_x = True

gem_speed = .5

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    gem.x += gem_speed * c.get_time()
    if gem.center_x <= wiz1.center_x:
        gem_speed = .5
    elif gem.center_x >= wiz2.center_x:
        gem_speed = -.5

    # Animate the wizard closest to the gem

    if gem.center_x < 509: 
        wiz1.image_animation_rate = 30
        wiz2.image_animation_rate = 0

    else:
        wiz1.image_animation_rate = 0
        wiz2.image_animation_rate = 30


    wiz1.update(c.get_time())
    wiz2.update(c.get_time())
    background.draw()
    wiz1.draw()
    wiz2.draw()
    gem.draw()

    pygame.display.flip()
    c.tick(30)