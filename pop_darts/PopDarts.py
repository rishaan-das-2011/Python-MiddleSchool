"""
LESSON: 6.3 - Complex Parameters
EXERCISE: Pop Darts
"""

#### ---- LIBRARIES ---- ####
import tsk
import random
import pygame
pygame.init()

#### ----------------------- ####
#### ---- SPAWN BALLOON ---- ####
#### ----------------------- ####

# DEFINE the spawn_balloon function with PARAMETERS
# sprite_list and direction

def spawn_balloon(sprite_list, direction):

    # Assign random_x a random int between 0 and 1000

    random_x = random.randint(0, 1000)

    # Assign random_y a random int between 0 and 150

    random_y = random.randint(0, 150)

    # Assign balloon a sprite using image
    # "BalloonAngry.png" at location random_x, random_y

    balloon = tsk.Sprite("BalloonAngry.png", random_x, random_y)

    # Append balloon to sprite_list
    # ---> TEST AFTER THIS LINE <--- #

    sprite_list.append(balloon)

    # If random_x is less than 500

    if random_x < 500:

        # Append "r" to the direction list

        direction.append("r")

    # Else

    else:

        # Append "l" to the direction list
        # ---> TEST AFTER THIS LINE <--- #

        direction.append("l")

#### ----------------------- ####
#### ---- MOVE BALLOONS ---- ####
#### ----------------------- ####

# DEFINE function move_balloons with PARAMETERS
# sprite_list, direction, and speed

def move_balloons(sprite_list, direction, speed):

    # For i in range length of sprite_list

    for i in range(len(sprite_list)):

        # Assign balloon the value from sprite_list at
        # index i

        balloon = sprite_list[i]

        # If the value at index i of direction list is
        # "r"

        if direction[i] == "r":

            # Increment balloon's x by speed
            # ---> TEST AFTER THIS LINE <--- #

            balloon.x += speed
    
            # If balloon's center_x is more than 1018

            if balloon.center_x > 1018:

                # Set the value at index i of direction
                # list to "l"
                # ---> TEST AFTER THIS LINE <--- #

                direction[i] = "l"

        # Else

        else:

            # Decrement balloon's x by speed
            # ---> TEST AFTER THIS LINE <--- #

            balloon.x -= speed
    
            # If balloon's center_x is less than 0

            if balloon.center_x < 0:

                # Set the value at index i of direction
                # list to "r"
                # ---> TEST AFTER THIS LINE <--- #

                direction[i] = "r"

#### -------------------------- ####
#### ---- DESTROY BALLOONS ---- ####
#### -------------------------- ####

# DEFINE function destroy_balloons with PARAMETERS
# sprite_list and dart

def destroy_balloons(sprite_list, dart):

    # Assign to_remove an empty list

    to_remove = []

    # For each balloon in sprite_list

    for balloon in sprite_list:

        # If the balloon collides with dart

        if pygame.sprite.collide_rect(balloon, dart):

            # Append ballon to to_remove list

            to_remove.append(balloon)

    # For each balloon in to_remove

    for balloon in to_remove:

        # Remove balloon from sprite_list

        sprite_list.remove(balloon)

    # RETURN the length of to_remove
    # ---> TEST AFTER THIS LINE <--- #

    return len(to_remove)

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# --- Setup --- #
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# --- Sprites --- #
background = tsk.Sprite("FairBooth.jpg", 0, 0)
dart = tsk.Sprite("Dart.png", 500, 450)
balloons = []
move_direction = []

# --- Variables --- #
balloon_timer = 2000
game_timer = 20000
num_balloons = 0
popped = 0
darts = 0
flying = False


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            flying = False

        elif event.type == pygame.MOUSEBUTTONUP:
            flying = True
            darts += 1

    # --- Dart follows mouse or flies forward --- #
    if not flying:
        x, y = pygame.mouse.get_pos()
        dart.center_x = x
        dart.center_y = 450

    else:
        dart.center_y -= .6 * c.get_time()

    # --- Dart resets if it gets too far --- #
    if dart.y < 0:
        flying = False

    # --- Balloons spawn every 2 seconds (up to 9) --- #

    # If balloon_timer is less than or equal to 0 and
    # num_balloons is less than 10

    if balloon_timer <= 0 and num_balloons < 10:

        # CALL spawn_balloon function with ARGUMENTS
        # balloons and move_direction

        spawn_balloon(balloons, move_direction)
    
        # Increment num_balloons by 1

        num_balloons += 1

        # Set balloon_timer to 2000
        # ---> TEST AFTER THIS LINE <--- #

        balloon_timer = 2000

    # --- Move balloon --- #

    # Assign speed the value .3 * c.get_time()

    speed = 0.3 * c.get_time()

    # CALL the move_balloons function with ARGUMENTS
    # balloons, move_direction, and speed

    move_balloons(balloons, move_direction, speed)

    # --- Pop balloons --- #

    # CALL the destroy_balloons function with ARGUMENTS
    # balloons and dart, and assign result to destroyed

    destroyed = destroy_balloons(balloons, dart)

    # Decrement num_balloons by destroyed

    num_balloons -= destroyed

    # Increment popped by destroyed
    # ---> TEST AFTER THIS LINE <--- #

    popped += destroyed

    #### ---- DRAW ---- ####

    # --- Draw scene --- #
    background.draw()
    for sprite in balloons:
        sprite.draw()
    dart.draw()

    # --- Finish --- #
    balloon_timer -= c.get_time()
    game_timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)

    if game_timer <= 0:
        drawing = False


#### ---- FINAL OUTPUT ---- ####
print("You popped " + str(popped) + " balloons")
print("You used " + str(darts) + " darts")



# Turn in your Coding Exercise.
