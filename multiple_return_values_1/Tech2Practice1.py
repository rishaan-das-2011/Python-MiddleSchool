"""
LESSON: 6.2 - Return Values
TECHNIQUE 2: Multiple Return Values
PRACTICE 1
"""

#### ---- LIBRARIES ---- ####
import pygame
import tsk
pygame.init()

#### ------------------- ####
#### ---- MOVE SHIP ---- ####
#### ------------------- ####
def move_ship(curr_x, curr_image, speed):
    # If ship is yellow, move left
    if curr_image == "RoundShip.png":
        new_x = curr_x - speed
        if new_x <= 0:
            new_image = "RoundShipPurple.png"
            going_left = False
        else:
            new_image = "RoundShip.png"
            going_left = True

    # If ship is purple, move right
    else:
        new_x = curr_x + speed
        if new_x >= 1018:
            new_image = "RoundShip.png"
            going_left = True
        else:
            new_image = "RoundShipPurple.png"
            going_left = False

    # Return information
    return new_x, new_image, going_left

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# Setup
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Sprites
background = tsk.Sprite("Space.jpg", 0, 0)
ship = tsk.Sprite("RoundShip.png", 500, 200)
ship.flip_x = True

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Move
    speed = 0.5 * c.get_time()
    new_x, new_image, going_left = move_ship(ship.center_x, ship.image, speed)
    ship.center_x = new_x
    ship.image = new_image
    ship.flip_x = going_left

    # Draw
    background.draw()
    ship.draw()

    # Finish
    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
