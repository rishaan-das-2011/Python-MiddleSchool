"""
LESSON: 5.4 - Sprites in Lists
TECHNIQUE 2: Row of Sprites
PRACTICE 2
"""

import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("SkyMountains.jpg", 0, 0)
sprite_list = [background]

filenames = ["Puffin0.png", "Puffin1.png", "Puffin2.png", "Puffin3.png", "Puffin4.png", "Puffin5.png", "Puffin6.png", "Puffin7.png"]

for i in range (8):
    sprite = tsk.Sprite(filenames[i], 40 + 120 * i, 200)
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


# Turn in your Coding Exercise.
