"""
LESSON: Sky Dodge Project
EXERCISE: Scroller
"""

# Place the comments below in the numbered locations
# based on the code that they describe. You will use
# each comment exactly once.

# Draw background
# Random cloud
# Move clouds
# Track clouds
# Cloud variables
# Clouds have a max spawn speed
# Program variables
# Remove
# Set new timing
# Mark for removal
# Move background
# Draw clouds

#### ---- LIBRARIES ---- ####

import random
import tsk
import pygame
pygame.init()


#### ---- VARIABLES ---- ####

# 1:
window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("SkyScrolling.jpg", 0, 0)
c = pygame.time.Clock()


# 2:
clouds = []
cloud_names = ["Cloud1.png", "Cloud2.png", "Cloud3.png"]
time_between_clouds = 3500
cloud_timer = 0
cloud_move_speed = .2


#### ---- MAIN LOOP ---- ####

game_over = False
while not game_over:


    #### ---- EVENT LOOP ---- ####

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    #### ---- SPAWN NEW SPRITES ---- ####

    cloud_timer += c.get_time()
    if cloud_timer > time_between_clouds:

        # 3:
        random_index = random.randint(0, len(cloud_names) - 1)
        image = cloud_names[random_index]
        cloud = tsk.Sprite(image, 1020, random.randint(-10, 550))

        # 4:
        clouds.append(cloud)

        # 5:
        cloud_timer = 0
        time_between_clouds -= 50


    #### --- SCROLL SCREEN --- ####

    # 6:
    background.center_x -= .1 * c.get_time()
    if background.center_x <= 0:
        background.center_x = 1018

    # 7:
    for cloud in clouds:
        cloud.center_x -= cloud_move_speed * c.get_time()


    #### ---- REMOVE OFF-SCREEN SPRITES ---- ####

    old_clouds = []

    # 8:
    for cloud in clouds:
        if cloud.center_x < -100:
            old_clouds.append(cloud)

    # 9:
    for cloud in old_clouds:
        clouds.remove(cloud)


    #### ---- DRAW FRAME ---- ####

    # 10:
    background.draw()

    # 11:
    for cloud in clouds:
        cloud.draw()

    pygame.display.flip()


    #### ---- TIME & SCORE ---- ####

    c.tick(30)

    # 12:
    if time_between_clouds < 750:
        time_between_clouds = 750
