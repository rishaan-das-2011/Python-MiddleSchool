"""
LESSON: 6.1 - Functions
WARMUP 5
"""

# Libraries
import random
import tsk
import pygame
pygame.init()


#### ---------------------------- ####
#### ---- DRAW FOOD FUNCTION ---- ####
#### ---------------------------- ####

def food(number, food_names):
    if 1 <= number <= 5:
        item = tsk.Sprite(food_names[number - 1], random.randint(150, 868), random.randint(400, 500))
        return item
    
    else:
        return None 
    







#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("Restaurant.jpg", 0, 0)
background.draw()
pygame.display.flip()

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Get input
    value = int(input("Enter a number, 1 - 5 or 0 to quit "))

    # Call function here
    if value != 0:
        food_item = food(value, food_names)
        if food_item:
            food_item.draw()
    

    # Finish
    pygame.display.flip()
    if value == 0:
        drawing = False

