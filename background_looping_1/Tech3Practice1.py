"""
LESSON: 5.1 - Sprites
TECHNIQUE 3: Background Looping
PRACTICE 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

background1 = tsk.Sprite("WinterHills.png", 0, 0)
background2 = tsk.Sprite("WinterHills.png", 1018, 0)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background1.x -= 5
    background2.x -= 5
    
    
    
    if background1.rect.x <= -1018:
        background1.rect.x = 1018
    if background2.rect.x <= -1018:
        background2.rect.x = 1018

    background1.draw()
    background2.draw()
    pygame.display.flip()


# Turn in your Coding Exercise.
