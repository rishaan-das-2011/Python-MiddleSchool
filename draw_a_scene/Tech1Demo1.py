"""
LESSON: 5.4 - Sprites in Lists
TECHNIQUE 1: Draw Scene
DEMO 1
"""

import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Desert.jpg", 0, 0)
crab = tsk.Sprite("RockCrab.png", 230, 250)
rock1 = tsk.Sprite("BrownRock1.png", 100, 200)
rock2 = tsk.Sprite("BrownRock2.png", 400, 350)
rock3 = tsk.Sprite("BrownRock3.png", 700, 100)
rock4 = tsk.Sprite("RoundGemPink.png", 700, 400)


tornado_sheet = tsk.ImageSheet("DustTornadoSheet.png", 4, 5)
tornado = tsk.Sprite(tornado_sheet, -250, 185)
tornado.image_animation_rate = 10
sprite_list = [background, crab, rock1, rock3, rock4, tornado, rock2]



drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    tornado.center_x += 0.2 * c.get_time()
    for sprite in sprite_list:
        sprite.draw()





    pygame.display.flip()
    c.tick(30)