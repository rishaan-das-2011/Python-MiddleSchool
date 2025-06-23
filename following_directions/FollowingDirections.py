"""
LESSON: 6.1 - Functions
EXERCISE: Following Directions
"""

#### ---- LIBRARIES ---- ####
import tsk
import random
import pygame
pygame.init()


#### ----------------------------- ####
#### ---- DRAW ARROW FUNCTION ---- ####
#### ----------------------------- ####

# DEFINE the draw_arrow function with PARAMETERS
# window, direction, and color

def draw_arrow(window, direction, color):

    # — Arrow body — #
    # If the direction is "left" or "right"
    
    if direction == "left" or direction == "right":
        
        # Create a Rect called body_rect that starts at
        # (600, 200) and is 200 pixels wide and 100
        # pixels tall
        
        body_rect = pygame.Rect(600, 200, 200, 100)
        
    # Else
    
    else:
        
        # Create a Rect called body_rect that starts at
        # (600, 200) and is 100 pixels wide and 200
        # pixels tall
        
        body_rect = pygame.Rect(600, 200, 100, 200)

    # — Arrow point — #
    # If the direction is "left"
    
    if direction == "left":
        
        # Create a point called far with value
        # (450, 250)
        
        far = (450, 250)
        
        # Create a point called base1 with value
        # (600, 150)
        
        base1 = (600, 150)
        
        # Create a point called base2 with value
        # (600, 350)
        
        base2 = (600, 350)
    
    # Else if the direction is "right"
    
    elif direction == "right":
        
        # Create point far with value (950, 250)
        
        far = (950, 250)
        
        # Create point base1 with value (800, 150)
        
        base1 = (800, 150)
        
        # Create point base2 with value (800, 350)
        
        base2 = (800, 350)
        
    
    # Else if the direction is "up"
    elif direction == "up":
        # Create point far with value (650, 50)
        far = (650, 50)
        # Create point base1 with value (550, 200)
        base1 = (550, 200)
        # Create point base2 with value (750, 200)
        base2 = (750, 200)
    
    # Else if direction is "down"
    elif direction == "down":
        # Create point far with value (650, 550)
        far = (650, 550)
        # Create point base1 with value (550, 400)
        base1 = (550, 400)
        # Create point base2 with value (750, 400)
        base2 = (750, 400)

    # — Arrow color — #
    # If color is "green"
    if color == "green":
        # Create color draw_color with the tuple for
        # green
        draw_color = (0, 255, 0)
    # Else if the color is "red"
    elif color == "red":
        # Create color draw_color with the tuple for
        # red
        draw_color = (255, 0, 0)

    # — Draw arrow — #
    # Draw rect body_rect in window using draw_color
    pygame.draw.rect(window, draw_color, body_rect)
    # Draw a polygon in window using draw_color and the
    # points far, base1, and base2
    pygame.draw.polygon(window, draw_color, [far, base1, base2])


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

#### ---- SETUP ---- ####
# — Program setup — #

w = pygame.display.set_mode([1018, 573])

c = pygame.time.Clock()

# — Sprites — #
background = tsk.Sprite("ScienceLab.jpg", 0, 0)
robot = tsk.Sprite("RobotDance.png", 100, 150)

# — Arrow setup — #
arrow = "left"
arrow_color = "red"
arrow_timer = 0
arrow_limit = 1000
directions = ["left", "right", "up", "down"]

# — Score variables — #

score = 0
mistakes = 0


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    #### ---- EVENT LOOP ---- ####
    for event in pygame.event.get():

        # — Quit — #
        if event.type == pygame.QUIT:
            drawing = False

        # — Key Press — #
        # If the event type is KEYDOWN
        if event.type == pygame.KEYDOWN:

            # If the event key is K_RIGHT and arrow is
            # "right" or the event key is K_LEFT and
            # arrow is "left" or the event key is
            # K_DOWN and arrow is "down" or the event
            # key is K_UP and arrow is "up"
            if ((event.key == pygame.K_RIGHT and arrow == "right") or
                (event.key == pygame.K_LEFT and arrow == "left") or
                (event.key == pygame.K_DOWN and arrow == "down") or
                (event.key == pygame.K_UP and arrow == "up")):

                # Set arrow_color to "green"
                arrow_color = "green"

                # Increment score by 1
                score += 1

            # Otherwise
            else:
                # Increment mistakes by 1
                mistakes += 1


    #### ---- ARROW ---- ####

    # — Switch to new arrow if necessary — #
    # If arrow_timer is greater than or equal to
    # arrow_limit
    if arrow_timer >= arrow_limit:

        # — Lose a try if you missed the arrow — #
        # If arrow_color is still "red"
        if arrow_color == "red":
            # Increment mistakes by 1
            mistakes += 1

        # — New direction — #
        # Set rand_arrow to a random integer between 0
        # and 3
        rand_arrow = random.randint(0, 3)

        # Set arrow to the item from list directions
        # at index rand_arrow
        arrow = directions[rand_arrow]

        # — Re-set color — #
        # Set arrow_color to "red"
        arrow_color = "red"

        # — Re-set and reduce time limit – #
        # Set arrow_timer to 0
        arrow_timer = 0

        # If arrow_limit is greater than 500
        if arrow_limit > 500:
            # Decrement arrow_limit by 10
            arrow_limit -= 10


    #### ---- DRAW SCENE ---- ####

    background.draw()
    robot.draw()

    # CALL the draw_arrow function with w, arrow, and
    # the arrow_color
    
    draw_arrow(w, arrow, arrow_color)


    #### ---- FINISH ---- ####

    # Increment arrow_timer by c.get_time()
    arrow_timer += c.get_time()

    pygame.display.flip()
    c.tick(30)

    # If mistakes is greater than or equal to 5
    if mistakes >= 5:
        # Set drawing to False
        drawing = False


#### ---- FINAL OUTPUT ---- ####

# Print "Your final score was: " with the score
# converted to a string
print("Your final score was: " + str(score))


# Turn in your Coding Exercise.



