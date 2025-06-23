"""
LESSON: 5.2 - Spritesheet Animation
TECHNIQUE 2: Smooth Movement
PRACTICE 2
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
clock = pygame.time.Clock()

background = tsk.Sprite("OutdoorPlowedField.jpg", 0, 0)
butterfly = tsk.Sprite("Butterfly.png", 0, 300)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    c = clock.tick(30)

    butterfly.x += 0.18 * c
    butterfly.y -= 0.1 * c


    background.draw()
    butterfly.draw()

    pygame.display.flip()
    


# Turn in your Coding Exercise.
