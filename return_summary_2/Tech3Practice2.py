"""
LESSON: 6.3 - Complex Parameters
TECHNIQUE 3: Return Summary
PRACTICE 2
"""

#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()

#### ------------------------------- ####
#### ---- MAKE BUBBLES FUNCTION ---- ####
#### ------------------------------- ####
def make_bubbles(bubbles, speed_tuples):

    old_bubbles = []
    x, y = pygame.mouse.get_pos()

    for sprite in bubbles:
        if sprite.rect.collidepoint(x, y):

            # Mark old bubbles
            old_bubbles.append(sprite)

            # Add new bubbles
            bubb1 = tsk.Sprite("Bubble.png", sprite.x, sprite.y)
            bubb2 = tsk.Sprite("Bubble.png", sprite.center_x, sprite.center_y)

            bubb1.scale = .5 * sprite.scale
            bubb2.scale = bubb1.scale

            bubbles.append(bubb1)
            bubbles.append(bubb2)

            # Add new speeds for the bubbles
            rand_x = random.randint(5, 15) / 100
            rand_y = random.randint(5, 15) / 100

            rand_speed1 = (rand_x, rand_y)
            rand_speed2 = (rand_x * -1, rand_y * -1)

            speed_tuples.append(rand_speed1)
            speed_tuples.append(rand_speed2)

    # Remove old bubbles
    for bubble_to_remove in old_bubbles:
        curr_index = bubbles.index(bubble_to_remove)
        speed_tuples.remove(speed_tuples[curr_index])
        bubbles.remove(bubble_to_remove)

    # Return number of bubbles split (removed)

    return len(old_bubbles)

#### ------------------------------- ####
#### ---- MOVE BUBBLES FUNCTION ---- ####
#### ------------------------------- ####
def move_bubbles(bubbles, speed_tuples, clock):

    # Check all bubbles
    for bubble in bubbles:

        # Get current bubble speeds
        curr_index = bubbles.index(bubble)
        x_speed, y_speed = speed_tuples[curr_index]

        # Move the bubble
        bubble.x += x_speed * clock.get_time()
        bubble.y += y_speed * clock.get_time()

        # Check for bounces
        if bubble.center_x > 1018 or bubble.center_x < 0:
            x_speed = x_speed * -1
        if bubble.center_y > 573 or bubble.center_y < 0:
            y_speed = y_speed * -1

        # Re-set speed if it has changed
        speed_tuples[curr_index] = (x_speed, y_speed)


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

#### ---- SETUP ---- ####

# Program
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Sprites
background = tsk.Sprite("LakeSideView.jpg", 0, 0)
first_bubble = tsk.Sprite("Bubble.png", 500, 100)
first_bubble.scale = 3

# Tracking
bubbles = [first_bubble]
speeds = [(.1, .15)]
splits = 0


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Update bubbles
    splits += make_bubbles(bubbles, speeds)                       
    move_bubbles(bubbles, speeds, c)

    # Draw bubbles
    background.draw()
    for sprite in bubbles:
        sprite.draw()

    # Finish
    pygame.display.flip()
    c.tick(30)


#### ---- FINAL OUTPUT ---- ####
print("You split " + str(splits) + " bubbles")


# Turn in your Coding Exercise.
