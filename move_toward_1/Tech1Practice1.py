"""
LESSON: 6.3 - Complex Parameters
TECHNIQUE 1: Move Toward
PRACTICE 1
"""

#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()

#### ---------------------------- ####
#### ---- MOVE STAR FUNCTION ---- ####
#### ---------------------------- ####

def move_star(star, ship, speed):
    
    # Calculate horizontal movement
    
    x = star.center_x
    if ship.center_x < x - 2:
        x -= speed
        
    elif ship.center_x > x + 2:
        x += speed
        
    # Calculate vertical movement
    
    y = star.center_y
    if ship.center_y < y - 2:
        y -= speed
        
    elif ship.center_y > y + 2:
        y += speed
        
    # Move star
    
    star.center = (x, y)
    
    return
#### ---------------------------- ####
#### ---- MOVE SHIP FUNCTION ---- ####
#### ---------------------------- ####

def move_ship(ship, speed, up):
    
    # If ship is moving up
    
    if up:
        
        ship.center_y -= speed
        
        # If ship has hit top, return False to show
        # we are no longer moving up
        
        if ship.center_y <= 0:
            ship.center_y = 0
            return False
        
    # If ship is moving down
    
    else:
        ship.center_y += speed
        
        # If ship has hit bottom, return True to show
        # that we are now moving up
        
        if ship.center_y >= 573:
            ship.center_y = 573
            return True
        
    return up

#### ----------------------------- ####
#### ---- SPAWN STAR FUNCTION ---- ####
#### ----------------------------- ####
def spawn_star(all_stars):
    # Pick the left or right star
    x = random.choice([0, 982])
    y = random.randint(0, 537)
    star = tsk.Sprite("Star.png", x, y)
    all_stars.append(star)
#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()
# Sprites
background = tsk.Sprite("AlienSpace.jpg", 0, 0)
ship = tsk.Sprite("RoundShip.png", 450, 200)
# Other variables
moving_up = True
stars = []
star_timer = 1000
#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
    # Create stars
    if star_timer <= 0:
        spawn_star(stars)
        star_timer = 1000
    # Move sprites
    for star in stars:
        move_star(star, ship, .1 * c.get_time())
    moving_up = move_ship(ship, .3 * c.get_time(), moving_up)
    # Draw
    background.draw()
    ship.draw()
    for star in stars:
        star.draw()
    # Finish
    star_timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)
    
# Turn in your Coding Exercise.
