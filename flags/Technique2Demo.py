"""
LESSON: 6.1 - Functions
TECHNIQUE 2: Flags
DEMO
"""

#### ---- LIBRARIES --- ####
import tsk
import random
import pygame
pygame.init()

#### --------------------------- ####
#### ---- DRAW BUG FUNCTION ---- ####
#### --------------------------- ####
def draw_bug(is_large, bug_type):
    x = random.randint(0, 950)
    y = random.randint(0, 500)

    bug = tsk.Sprite("Bee.png", x, y)

    # Add boolean flag - check if bug should be large or small 

    if is_large:
        bug.scale = 2
    else:
        bug.scale = 0.5

    # Add integer flag - check which bug image will be used

    if bug_type == 1:
        bug.image = "Bee.png"
    elif bug_type == 2:
        bug.image = "Butterfly.png"
    else:
        bug.image = "Fly.png"


    bug.draw()


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# Setup
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("OutdoorBushes.jpg", 0, 0)
background.draw()

# Main loop
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # Key presses
        elif event.type == pygame.KEYDOWN:

            # Get a random integer to determine bug image

            num = random.randint(1, 3)
            
            if event.key == pygame.K_UP:
                draw_bug(True, num)
            elif event.key == pygame.K_DOWN:
                draw_bug(False, num)


    pygame.display.flip()