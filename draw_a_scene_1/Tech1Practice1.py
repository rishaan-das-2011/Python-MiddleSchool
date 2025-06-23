"""
LESSON: 5.4 - Sprites in Lists
TECHNIQUE 1: Draw Scene
PRACTICE 1
"""

import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("EmptySky.png", 0, 0)
foreground = tsk.Sprite("HillsGrassy.png", 0, 0)
bush1 = tsk.Sprite("BushesLeft.png", 0, 200)
bush2 = tsk.Sprite("BushesRight.png", 600, 200)
pony_sheet = tsk.ImageSheet("PonyRun.png", 5, 6)
sprite_list = [background, foreground, bush1, bush2]


for i in range(7):
    s = tsk.Sprite(pony_sheet, random.randint(40, 858), random.randint(330, 450))
    s.image_animation_rate = random.randint(5, 60)

    # Add the newly-created ponies to the list of sprites

    sprite_list.append(s)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Animate & draw sprites

    for sprite in sprite_list:
        sprite.update(c.get_time())
        sprite.draw()

    c.tick(30)
    pygame.display.flip()


# Turn in your Coding Exercise.
