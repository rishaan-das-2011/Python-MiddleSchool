"""
LESSON: 6.3 - Complex Parameters
TECHNIQUE 1: Move Toward
PRACTICE 2
"""

#### ---- LIBRARIES ---- ####
import tsk
import pygame
pygame.init()


#### -------------------------------- ####
#### ---- MOVE TO MOUSE FUNCTION ---- ####
#### -------------------------------- ####
def move_to_mouse(sprite, speed):

    # Get the mouse position (goal) and sprite center
    # position (start)
    goal_x, goal_y = pygame.mouse.get_pos()
    start_x, start_y = sprite.center


    # Calculate new x position
    x = sprite.center_x
    if goal_x < x - 2:
        x -= speed
    elif goal_x > x + 2:
        x += speed




    # Calculate new y position
    y = sprite.center_y
    if goal_y < y - 2:
        y -= speed
    elif goal_y > y + 2:
        y += speed




    # Move sprite towards new position
    sprite.center_y = y
    sprite.center_x = x



#### ------------------------------ ####
#### ---- SPAWN GHOST FUNCTION ---- ####
#### ------------------------------ ####
def spawn_ghost(all_ghosts):
    ghost = tsk.Sprite("Ghost.png", 0, 0)
    ghost.center = (100, 250)
    all_ghosts.append(ghost)


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Sprites
background = tsk.Sprite("HauntedForest.jpg", 0, 0)
tower = tsk.Sprite("SkullTower.png", -100, 150)
ghosts = []

# Other variables
ghost_timer = 1000

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Create a ghost
    if ghost_timer <= 0:
        spawn_ghost(ghosts)
        ghost_timer = 5000

    # Move sprites
    for ghost in ghosts:
        move_to_mouse(ghost, .08 * c.get_time())

    # Draw
    background.draw()
    tower.draw()
    for ghost in ghosts:
        ghost.draw()

    # Finish
    ghost_timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
