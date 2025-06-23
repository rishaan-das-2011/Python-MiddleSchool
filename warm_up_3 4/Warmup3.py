"""
LESSON: 5.4 - Sprites in Lists
WARMUP 3
"""

import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("LivingRoom.jpg", 0, 0)

vases = []
start_y = 0

for i in range(5):
    x = random.randint(0, 950)
    y = random.randint(start_y, start_y + 100)
    start_y = y

    # Create vase sprites

    vase = tsk.Sprite("BushVase3.png", x, y)
    vases.append(vase)


drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.draw()

    # Draw vases
    for vase in vases:
        vase.draw()


    pygame.display.flip()
