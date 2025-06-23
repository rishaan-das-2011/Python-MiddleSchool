"""
LESSON: 5.1 - Sprites
TECHNIQUE 1: Make a Sprite
DEMO
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

# Declare sprite here

cat = tsk.Sprite("Cat.png", 100, 100)
unicorn = tsk.Sprite("AstronautSpin.png", 500, 100)
drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False  

    window.fill((0, 0, 0))

    # Draw sprite here
    cat.draw()
    unicorn.draw()
    pygame.display.flip()