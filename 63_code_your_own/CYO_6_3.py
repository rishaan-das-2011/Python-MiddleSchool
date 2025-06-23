"""
EXERCISE: Final Project

TITLE: [Food Clicker Game]
DESCRIPTION: [A program where user clicks on list of foods to eat and then 
generates a summary.]
"""

import random
import tsk
import pygame


pygame.init()


window = pygame.display.set_mode([1000, 600])


# Define color constants

white = (255, 255, 255)
black = (0, 0, 0)

# Create background and food sprites

background = tsk.Sprite("ComicBackgroundFlash.png", 0, 0)
pizza_image = tsk.Sprite("PizzaWhole.png", 600, 0)
burger_image = tsk.Sprite("Burger.png", 100, 0)
fries_image = tsk.Sprite("FrenchFries.png", 0, 400)
taco_image = tsk.Sprite("Taco.png", 0, 200)
juice_image = tsk.Sprite("OrangeJuice.png", 300, 300)

# List containing different food images

all_foods = [pizza_image, burger_image, fries_image, taco_image, juice_image]


# Create a clock to control frame rate

clock = pygame.time.Clock()


# Initialize food counter and dict

food_count = 0
food_clicked = {} # To store clicked foods

#### ------------------------------------####
#### ---- SHOW INSTRUCTION FUNCTION ---- ####
#### ----------------------------------- ####
def show_instructions():
    print("Click on a food to eat!")
    print("If you do not click on any food then you at least have a drink.")

#### ------------------------------------####
#### ---- FOOD SUMMARY FUNCTION -------- ####
#### ----------------------------------- ####
def generate_food_list():
    food_list = list(map(list, food_clicked.items()))
    food_list_string = ""
    for i in range(len(food_list)):
        food_list_string = food_list_string + ' = '.join(map(str, food_list[i])) + "\n"
    return food_list_string  # Return updated count

#### --------------------------- ####
#### ---- GET NAME FUNCTION ---- ####
#### --------------------------- ####
def get_name(imageName="OrangeJuice.png"):
    if imageName == "PizzaWhole.png":
        return "\nPizza"
    elif imageName == "Burger.png":
        return "\nBurger"
    elif imageName == "FrenchFries.png":
        return "\nFrenchFries"
    elif imageName == "Taco.png":
        return "\nTaco"
    elif imageName == "OrangeJuice.png":
        return "\nOrangeJuice"


# Show game instructions at start

show_instructions()


# -------- Main Game Loop ----------

running = True
while running:
    window.fill((255, 255, 255))

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check if click was on any food, then add it to dict
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for food in all_foods:
                if food.rect.collidepoint(x, y):
                    food_count += 1
                    name = get_name(food.image)
                    food_clicked[name] = food_clicked.get(name, 0) + 1
                    print(name + " clicked!")

    # Draw
    background.draw()
    for food in all_foods:
        food.draw()
    juice_image.draw()
 
    pygame.display.flip()
    clock.tick(30)


#### ---- FINAL OUTPUT ---- ####
print("You clicked " + str(food_count) + " times")
# If you do not click on any food, then the orange juice will be added by default
if food_count == 0:
    name = get_name() 
    food_clicked[name] = food_clicked.get(name, 0) + 1 

# print the summary
print(generate_food_list())





# Turn in your Coding Exercise.
