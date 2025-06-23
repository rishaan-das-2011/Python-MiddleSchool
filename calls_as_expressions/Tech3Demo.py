"""
LESSON: 6.2 - Return Values
TECHNIQUE 3: Function Calls as Expressions
DEMO
"""

#### ---- LIBRARIES ---- ####
import tsk
import random
import pygame
pygame.init()


#### ------------------------------- ####
#### ---- GET BUG NAME FUNCTION ---- ####
#### ------------------------------- ####
def get_bug_name(num):
    if num == 1:
        return "Bee.png"
    else:
        return "Butterfly.png"


#### ------------------------------ ####
#### ---- GET BUG DIR FUNCTION ---- ####
#### ------------------------------ ####
def get_bug_dir(num):
    if num == 1:
        return True
    else:
        return False


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# Setup
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("OutdoorBushes.jpg", 0, 0)

# Sprites
all_bugs = []
num_sprites = random.randint(3, 15)
for i in range(num_sprites):
    """
    # Get image
    random_bug = random.randint(1, 2)
    bug_pic = get_bug_name(random_bug)

    # Get facing direction
    random_direction = random.randint(1, 2)
    bug_dir = get_bug_dir(random_direction)

    # Get location
    x = random.randint(0, 900)
    y = random.randint(0, 500)
    """
    # Make sprite
    bug = tsk.Sprite(get_bug_name(random.randint(1, 2)), random.randint(0, 900), random.randint(0, 500))
    bug.flip_x = get_bug_dir(random.randint(1, 2))
    all_bugs.append(bug)


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Draw
    background.draw()
    for bug in all_bugs:
        bug.draw()
    pygame.display.flip()