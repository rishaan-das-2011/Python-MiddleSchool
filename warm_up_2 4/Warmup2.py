"""
LESSON: 6.1 - Functions
WARMUP 2
"""

# Libraries
import random
import tsk
import pygame
pygame.init()


#### ----------------------------- ####
#### ---- MAKE NOISE FUNCTION ---- ####
#### ----------------------------- ####
def noise_function(dog, cat):
    noises = ["Meow", "Arrf"]
    if pygame.sprite.collide_rect(dog, cat):
        print(random.choice(noises))






#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# Program variables
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Sprites
background = tsk.Sprite("LivingRoom.jpg", 0, 0)
cat = tsk.Sprite("BoredCat.png", 0, 150)
dog = tsk.Sprite("Pug.png", 800, 400)
dog.flip_x = True

# Animation variables
cat_x_speed = .05
cat_y_speed = .07
dog_x_speed = -.05
dog_y_speed = -.07


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Move sprites
    cat.center_x += cat_x_speed * c.get_time()
    cat.center_y += cat_y_speed * c.get_time()
    dog.center_x += dog_x_speed * c.get_time()
    dog.center_y += dog_y_speed * c.get_time()

    # Call function here

    noise_function(dog, cat)

    # Bounce on edges
    if cat.center_x < 0 or cat.center_x > 1018:
        cat_x_speed = -cat_x_speed
        cat_y_speed = random.randint(25, 80) * .001
        cat.flip_x = not cat.flip_x

    elif cat.center_y < 150 or cat.center_y > 550:
        cat_y_speed = -cat_y_speed
        cat_x_speed = random.randint(25, 80) * .001

        # Don't change the cat's direction when
        # changing speed
        if cat.flip_x and cat_x_speed > 0:
            cat_x_speed = -cat_x_speed

    if dog.center_x < 0 or dog.center_x > 1018:
        dog_x_speed = -dog_x_speed
        dog_y_speed = random.randint(25, 80) * .001
        dog.flip_x = not dog.flip_x

    elif dog.center_y < 150 or dog.center_y > 550:
        dog_y_speed = -dog_y_speed
        dog_x_speed = random.randint(25, 80) * .001

        # Don't change the dog's direction when
        # changing speed
        if dog.flip_x and dog_x_speed > 0:
            dog_x_speed = -dog_x_speed

    # Draw frame
    background.draw()
    cat.draw()
    dog.draw()

    # Finish
    pygame.display.flip()
    c.tick(30)

