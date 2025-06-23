"""
LESSON: 5.3 - Sprite Collision
EXERCISE: Robot Manners
"""

#### ---- SET UP ---- ####

# --- Libraries --- #
import tsk
import random
import pygame
pygame.init()


# --- Variables --- #

# Program variables
window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Sprites
background = tsk.Sprite("SchoolHallway.jpg", 0, 0)
moving_robot = tsk.Sprite("Robot.png", 300, 100)
little_robot = tsk.Sprite("CardboardRobot.png", 50, 150)
big_robot = tsk.Sprite("FriendlyRobot.png", 700, 400)

# Animation variables
moving_right = True
moving_down = True
vertical_speed = 5
horizontal_speed = 5


#### ---- MAIN LOOP ---- ####

drawing = True
while drawing:


    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False


    # --- Move Robot --- #
    # The robot moves by movement_speed in a diagonal
    # direction, depending on whether moving_right and
    # moving_down are True.

    x, y = moving_robot.center
    prev_x = x
    prev_y = y

    if moving_right:
        x += horizontal_speed
        moving_robot.flip_x = False
    else:
        x -= horizontal_speed
        moving_robot.flip_x = True
    if moving_down:
        y += vertical_speed
    else:
        y -= vertical_speed

    moving_robot.center = (x, y)


    # --- Collision --- #

    # If the moving robot collides with another robot,
    # it apologizes and turns around.  It resets its
    # vertical and horizontal speeds randomly.


    #### ---- RE-STRUCTURE 1 ---- ####

    # Instead of checking their coordinates, use
    # COLLIDE_RECT to see if the moving_robot and
    # big_robot collided

    big_x, big_y = big_robot.center
    width = (big_robot.center_x - big_robot.x) * 2
    height = (big_robot.center_y - big_robot.y) * 2

    closeness_x = big_x - x
    closeness_y = big_y - y
    colliding_x = closeness_x < width and closeness_x > width * -1
    colliding_y = closeness_y < height and closeness_y > height * -1


    if colliding_x and colliding_y:
        print("Excuse me, good Sir!")
        moving_robot.center_x = prev_x
        moving_robot.center_y = prev_y
        moving_right = not moving_right
        moving_down = not moving_down
        horizontal_speed = random.randint(2, 7)
        vertical_speed = random.randint(2, 7)


    #### ---- RE-STRUCTURE 2 ---- ####

    # Instead of checking their coordinates, use
    # COLLIDE_RECT to see if the moving_robot and
    # little_robot collided

    little_x, little_y = little_robot.center
    width = (little_robot.center_x - little_robot.x) * 2
    height = (little_robot.center_y - little_robot.y) * 2

    closeness_x = little_x - x
    closeness_y = little_y - y
    colliding_x = closeness_x < width and closeness_x > width * -1
    colliding_y = closeness_y < height and closeness_y > height * -1

    if colliding_x and colliding_y:
        print("Sorry, Miss!  I'll just turn around.")
        moving_robot.center_x = prev_x
        moving_robot.center_y = prev_y
        moving_right = not moving_right
        moving_down = not moving_down
        horizontal_speed = random.randint(2, 7)
        vertical_speed = random.randint(2, 7)


    #### ---- RE-STRUCTURE 3 ---- ####

    # Combine the two collision checks above into one
    # using the or operator. (HINT: it may help to save
    # the collision results in boolean variables
    # instead of using them directly as conditions.)
    # Continue to say different apologies to each robot.

    collided_with_big = pygame.sprite.collide_rect(moving_robot, big_robot)
    collided_with_little = pygame.sprite.collide_rect(moving_robot, little_robot)

    if collided_with_big or collided_with_little:
        # Determine which robot was hit
        if collided_with_big:
            print("Excuse me, good Sir!")
        else:
            print("Sorry, Miss! I'll just turn around.")
        
        # Reset position and direction
        moving_robot.center = (prev_x, prev_y)
        moving_right = not moving_right
        moving_down = not moving_down
        horizontal_speed = random.randint(2, 7)
        vertical_speed = random.randint(2, 7)


    # --- Screen boundaries --- #

    if x < 0:
        moving_right = True
    if x > 1000:
        moving_right = False
    if y < 170:
        moving_down = True
    if y > 500:
        moving_down = False

    # --- Draw --- #

    background.draw()
    little_robot.draw()
    moving_robot.draw()
    big_robot.draw()
    pygame.display.flip()

    c.tick(30)


# Turn in your Coding Exercise.
