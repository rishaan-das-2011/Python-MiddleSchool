"""
LESSON: 5.4 - Sprites in Lists
TECHNIQUE 2: Row of Sprites
DEMO 1
"""

import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("CodeUI.jpg", 0, 0)
sprite_list = [background]
filenames = ["Gem1.png", "Gem2.png", "Gem3.png", "Gem4.png"]

for i in range (4):
    sprite = tsk.Sprite(filenames[i], 218 + 150 * i, 250)
    sprite_list.append(sprite)




drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    for sprite in sprite_list:
        sprite.draw()

    pygame.display.flip()
    c.tick(30)