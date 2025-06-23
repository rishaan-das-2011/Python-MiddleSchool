"""
LESSON: 6.3 - Complex Parameters
WARMUP 1
"""

#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()


#### --------------------------- ####
#### ---- RANDOM BACKGROUND ---- ####
#### --------------------------- ####

def background_name(backgrounds):
    list_bg = ["AlienSpace.jpg", "Hills.jpg", "SchoolHallway.jpg"]
    backgrounds765 = random.choice(list_bg)
    print("BACKGROUND CHANGE TO: " + backgrounds765)
    return backgrounds765








#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# Setup
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("Hills.jpg", 0, 0)

# Sprites
panda = tsk.Sprite("Panda.png", 100, 100)
rock = tsk.Sprite("BigMossyRock.png", 400, 20)
vase = tsk.Sprite("ShortVase.png", 670, 280)


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Change and print background image

            background765 = background_name(background)
            background = tsk.Sprite(background765, 0, 0)


    # Draw
    background.draw()
    rock.draw()
    panda.draw()
    vase.draw()
    pygame.display.flip()
