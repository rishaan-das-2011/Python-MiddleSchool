"""
LESSON: 6.1 - Functions
TECHNIQUE 3: Draw at Offset
PRACTICE 2
"""

#### ---- LIBRARIES ---- ####
import tsk
import pygame
pygame.init()

#### ----------------------------- ####
#### ---- DRAW WATER FUNCTION ---- ####
#### ----------------------------- ####

def draw_water(window, pug_x, pug_y):
    offsets = [(-35, -10), (-50, -20), (-25, 10), (-10, -15), (30, -30), (50, -10), (-25, -10), (10, 15)]
    
    for dx, dy in offsets:
        x = pug_x + dx
        y = pug_y + dy
        pygame.draw.circle(window, (0, 0, 255), (int(x), int(y)), 5)









#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("LivingRoom.jpg", 0, 0)
pug = tsk.Sprite("Pug.png", 0, 0)
pug.center_x = 500
pug.center_y = 300
x = int(pug.center_x)
y = int(pug.center_y)

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # Move pug to mouse position

            x, y = pygame.mouse.get_pos()
            pug.center = (x, y)


    # Draw
    background.draw()
    pug.draw()
    draw_water(w, pug.center_x, pug.center_y)
    
    pygame.display.flip()


# Turn in your Coding Exercise.
