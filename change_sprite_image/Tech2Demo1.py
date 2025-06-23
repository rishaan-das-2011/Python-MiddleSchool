"""
LESSON: 5.1 - Sprites
TECHNIQUE 2: Changing Sprite Image
DEMO 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

panda = tsk.Sprite("Panda.png", 300, 300)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            panda.image = "PandaGentleman.png"
        
        elif event.type == pygame.MOUSEBUTTONUP:
            panda.image = "Panda.png"


    window.fill((0, 0, 0))

    panda.draw()
    pygame.display.flip()