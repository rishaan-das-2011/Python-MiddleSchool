"""
LESSON: 5.4 - Sprites in Lists
TECHNIQUE 2: Row of Sprites
PRACTICE 1
"""

import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

sprite_list = []
switches = [False, False, False]

for i in range (3):
    sprite = tsk.Sprite("LightSwitch.png", 160 + 250 * i, 200)
    sprite_list.append(sprite)



drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(3):
                if sprite_list[i].rect.collidepoint(x, y):
                    switches[i] = not switches[i]

    color = [0, 0, 0]
    for i in range(3):
        if switches[i]:
            color[i] = 255
    window.fill((color[0], color[1], color[2]))

    for sprite in sprite_list:
        sprite.draw()

    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
