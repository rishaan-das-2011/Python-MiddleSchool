"""
LESSON: 5.1 - Sprites
TECHNIQUE 2: Changing Sprite Image
PRACTICE 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

puffin = tsk.Sprite("PuffinWalk.png", 300, 300)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            puffin.image = "PuffinFly.png"
            
        if event.type == pygame.MOUSEBUTTONUP:
            puffin.image = "PuffinWalk.png"
            


    window.fill((0, 0, 0))

    puffin.draw()
    pygame.display.flip()


# Turn in your Coding Exercise.
