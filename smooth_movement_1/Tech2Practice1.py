"""
LESSON: 5.2 - Spritesheet Animation
TECHNIQUE 2: Smooth Movement
PRACTICE 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Stage.png", 0, 0)
pug = tsk.Sprite("PugBee.png", 900, 250)
pug.flip_x = True

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False



    background.draw()
    pug.center_x -= 0.1 * c.get_time()
    pug.draw()


    pygame.display.flip()
    c.tick(100)

# Turn in your Coding Exercise.
