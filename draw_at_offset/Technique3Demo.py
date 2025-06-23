"""
LESSON: 6.1 - Functions
TECHNIQUE 3: Draw at Offset
DEMO
"""

#### ---- LIBRARIES ---- ####
import tsk
import pygame
pygame.init()


#### ---------------------- ####
#### ---- DRAW SPRITES ---- ####
#### ---------------------- ####
def draw_sprites(x, y):
    panda = tsk.Sprite("PandaPilot.png", 0, 0)
    puffin = tsk.Sprite("PuffinWalk.png", 0, 0)

    panda.center_x = x
    panda.center_y = y
    puffin.center_x = x
    puffin.center_y = y - 200

    panda.scale = 0.7
    puffin.scale = 0.7

    panda.draw()
    puffin.draw()


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("SkyMountains.jpg", 0, 0)
mouse_x = 0
mouse_y = 0

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # Mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw
    background.draw()
    draw_sprites(mouse_x, mouse_y)
    pygame.display.flip()