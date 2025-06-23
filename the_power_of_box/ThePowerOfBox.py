"""
LESSON: 6.1 - Functions
EXERCISE: The Power of Box
"""

#### ---- LIBRARIES ---- ####

# Import the random library

import random

# Import the tsk library

import tsk

# Import pygame

import pygame

# Initialize pygame

pygame.init()

#### ------------------------------- ####
#### ---- ATTRACT CATS FUNCTION ---- ####
#### ------------------------------- ####

# DEFINE the attract_cats function with PARAMETERS
# num_cats, x, and y

def attract_cats(num_cats, x, y):
    
    # — Validate input — #
    # If num_cats is less than 0
    
    if num_cats < 0:
        # Set num_cats to 0
        
        num_cats = 0

    # — Cat creation loop — #
    # Create a list called cat_names with filenames
    # "BoredCat.png", "BrownAndWhiteCat.png", "Cat.png",
    #  and "FluffyCat.png"
    
    cat_names = ["BoredCat.png", "BrownAndWhiteCat.png", "Cat.png", "FluffyCat.png"]

    # For i in range num_cats
    
    for i in range(num_cats):
        
        # — Get random location — #
        # Set cat_x to a random integer between x - 450
        # and x + 450
        
        cat_x = random.randint(x - 450, x + 450)
        
        # Set cat_y to a random integer between y - 200
        # and y + 200
        
        cat_y = random.randint(y - 200, y + 200)
        
        # If x - cat_x is more than -100 and less than
        # 100
        
        if -100 < (x - cat_x) < 100:
            # Increment cat_x by 200
            
            cat_x += 200

        # — Make cat — #
        # Assign index a random integer between 0 and
        # the length of cat_names - 1
        
        index = random.randint(0, len(cat_names) - 1)
        
        # Create a sprite called cat at (0, 0) with
        # the filename from cat_names at index
                               
        cat = tsk.Sprite(cat_names[index], 0, 0)
        
        # Set the cat's center to (cat_x, cat_y)
                               
        cat.center = (cat_x, cat_y)

        # — Flip cats on the right — #
        # If cat_x is more than x
                               
        if cat_x > x:
            # Set the cat's flip_x to True
                               
            cat.flip_x = True

        # — Draw cat — #
                               
        cat.draw()

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# Create a window called w with size [1018, 573]
                               
w = pygame.display.set_mode([1018, 573])

# — Background — #
# Create a sprite called background at (0, 0),
# using image "CatRoom.jpg"
                               
background = tsk.Sprite("CatRoom.jpg", 0, 0)

# Draw the background sprite
                               
background.draw()

# — Box — #
# Create a sprite called box at (0, 0) using image
# "CatBox.png"
box = tsk.Sprite("CatBox.png", 0, 0)
                               

# Set the box's center to (500, 300)
                               
box.center = (500, 300)

# Draw the box sprite
                               
box.draw()

# Flip the display
                               
pygame.display.flip()

#### ---- MAIN LOOP ---- ####


# Set drawing to True
                               
drawing = True

# Loop while drawing
                               
while drawing:
                               
    # — Event loop — #
    # Create an event loop
                               
    for event in pygame.event.get():
                               
        # Check for the QUIT event
                               
        if event.type == pygame.QUIT:
                               
            # Set drawing to False
                               
            drawing = False

    # — Get user input — #
    # Set variable more to the result of input with
    # prompt "More cats?! (enter or type stop) "
                               
    more = input("More cats?! (enter or type stop) ")

    # If more is equal to "stop"
                               
    if more == "stop":
                               
        # Set drawing to False
                               
        drawing = False

    # Else
                               
    else:
                               
        # CALL the attract_cats function with a random
        # integer between 1 and 7, and the box's
        # center_x and center_y
                               
        attract_cats(random.randint(1, 7), box.center_x, box.center_y)

    # — Finish — #
    # Flip the display
                               
        
    pygame.display.flip()



# Turn in your Coding Exercise.



