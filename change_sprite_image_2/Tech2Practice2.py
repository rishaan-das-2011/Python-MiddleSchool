"""
LESSON: 5.1 - Sprites
TECHNIQUE 2: Changing Sprite Image
PRACTICE 2
"""
import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])

panda = tsk.Sprite("Panda.png", 300, 100)
images = ["Panda.png", "PandaDuck.png", "PandaGentleman.png", "PandaPilot.png"]

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.KEYDOWN:
            new_image = images[random.randint(0, len(images) - 1)]
            panda.image = new_image
            print("Changing panda to image " + new_image) 

        

    window.fill((0, 0, 0))

    panda.draw()
    pygame.display.flip()


# Turn in your Coding Exercise.
