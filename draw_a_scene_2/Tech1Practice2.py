"""
LESSON: 5.4 - Sprites in Lists
TECHNIQUE 1: Draw Scene
PRACTICE 2
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("SkyMountains.jpg", 0, 0)
panda = tsk.Sprite("PandaDuckSmall.png", 50, 50)
butterfly = tsk.Sprite("Butterfly.png", 450, 330)
puffin = tsk.Sprite("PuffinFly.png", 600, 100)
bee = tsk.Sprite("Bee.png", 800, 250)

sprite_list = [background, panda, butterfly, puffin, bee]

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
