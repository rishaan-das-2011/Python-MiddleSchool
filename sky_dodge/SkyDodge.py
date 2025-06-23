"""
LESSON: Sky Dodge Project
"""

#### ---- LIBRARIES ---- ####

# E1: Import the random library

import random

# B1: Import the tsk library

import tsk

# A1: Import the pygame library

import pygame

# A2: Initialize pygame

pygame.init()

#### ---- VARIABLES ---- ####

# --- Program variables --- #

# A3: Create a window of size [1018, 573] called window

window = pygame.display.set_mode([1018, 573])

# B2: Create a SPRITE called background at (0, 0)
# using "SkyScrolling.jpg"

background = tsk.Sprite("SkyScrolling.jpg", 0, 0)

# C1: Create a Clock called c

c = pygame.time.Clock()

# --- Dragon variables --- #

# D1: Create an IMAGESHEET called dragon_sheet using
# "DragonFlying.png" with 4 rows and 6 columns

dragon_sheet = tsk.ImageSheet("DragonFlying.png", 4, 6)

# D2: Create a SPRITE called dragon using dragon_sheet
# at position (0, 0)

dragon = tsk.Sprite(dragon_sheet, 0, 0)

# D3: Create a dragon_move_speed variable set to .5

dragon_move_speed = 0.5

# --- Cloud variables --- #

# E2: Create an empty list called clouds

clouds = []

# E3: Create a list called cloud_names with the strings
# "Cloud1.png", "Cloud2.png", and "Cloud3.png"

cloud_names = ["Cloud1.png", "Cloud2.png", "Cloud3.png"]

# E4: Create a variable called time_between_clouds set
# to 3500

time_between_clouds = 3500

# E5: Create a variable called cloud_timer set to 0

cloud_timer = 0

# F1: Create a variable called cloud_move_speed set
# to .2

cloud_move_speed = 0.2

# --- Flame variables --- #

# I1: Create an IMAGESHEET called fire_sheet using
# "FireBlast.png" with 4 rows and 6 columns

fire_sheet = tsk.ImageSheet("FireBlast.png", 4, 6)

# I2: Create a SPRITE called flame using the fire_sheet
# at the dragon's CENTER_X + 90, and -100

flame = tsk.Sprite(fire_sheet, dragon.center_x + 90, -100)

# I3: Create a variable flame_on set to False

flame_on = False

# J1: Create a variable flame_timer set to 0

flame_timer = 0

# J2: Create a variable flame_duration set to 900

flame_duration = 900

# --- Balloon variables --- #

# K1: Create an empty list called balloons

balloons = []

# K2: Create a variable called time_between_balloons
# set to 5000

time_between_balloons = 5000

# K3: Create a variable called balloon_timer set to 0

balloon_timer = 0

# L1: Create a variable called balloon_move_speed set
# to .25

balloon_move_speed = 0.25

# --- Score variables --- #

# O1: Create a variable called distance set to 0.0

distance = 0.0

# P1: Create a variable called score set to 0

score = 0

#### ---- MAIN LOOP ---- ####

# A4: Create variable called game_over with value False

game_over = False

# A5: While not game_over

while not game_over:

    #### ---- EVENT LOOP ---- ####

    # A6: Create an event loop

    for event in pygame.event.get():

        # --- Quit --- #

        # A7: If the event type is QUIT

        if event.type == pygame.QUIT:

            # A8: Set game_over to True
            # ---> TEST AFTER THIS LINE <--- #

            game_over = True

        # --- Spacebar pressed --- #

        # I4: If the event type is KEYDOWN and the key
        # is K_SPACE

        if event.type == pygame.KEYDOWN and tsk.get_key_pressed(pygame.K_SPACE):

            # I5: Set flame to be a new SPRITE using
            # fire_sheet at the dragon's CENTER_X + 90
            # and the dragon's CENTER_Y

            flame = tsk.Sprite(fire_sheet, dragon.center_x + 90, dragon.center_y)

            # I6: Set flame_on to True

            flame_on = True

    #### ---- MOVE WITH ARROW KEYS ---- ####
    
    # D4: Use TSK.IS_KEY_DOWN to check if the K_UP key
    # is held down and the dragon's
    # CENTER_Y is not less than or equal to 0

    if tsk.is_key_down(pygame.K_UP) and dragon.center_y > 0:

        # D5: Decrement the dragon's CENTER_Y by
        # dragon_move_speed * c.get_time()

        dragon.center_y -= dragon_move_speed * c.get_time()

    # D6: Elif use TSK.IS_KEY_DOWN to check if K_DOWN
    # key is held down and the dragon's CENTER_Y is not
    # greater than or equal to 573

    elif tsk.is_key_down(pygame.K_DOWN) and dragon.center_y < 573:

        # D7: Increment the dragon's CENTER_Y by
        # dragon_move_speed * c.get_time()

        dragon.center_y += dragon_move_speed * c.get_time()

    #### ---- CHECK FOR COLLISIONS ---- ####

    # --- Dragon hits a cloud --- #

    # H1: For each cloud in the clouds list

    for cloud in clouds:

        # H2: If the cloud and dragon collide with
        # COLLIDE_RECT

        if pygame.sprite.collide_rect(cloud, dragon):

            # H3: Set game_over to True

            game_over = True
    
            # H4: Break
            # ---> TEST AFTER THIS LINE <--- #

            break

    # --- Flame hits a balloon --- #

    # N1: Create an empty list called balloons_to_remove

    balloons_to_remove = []

    # N2: For each balloon in the balloons list

    for balloon in balloons:

        # N3: If flame and balloon collide with
        # COLLIDE_RECT

        if pygame.sprite.collide_rect(flame, balloon):

            # N4: Append balloon to the
            # balloons_to_remove list

            balloons_to_remove.append(balloon)

            # P2: Increment score by 1

            score += 1

    # N5: For each balloon in balloons_to_remove

    for balloon in balloons_to_remove:

        # N6: Remove the balloon from the balloons list
        # ---> TEST AFTER THIS LINE <--- #

        balloons.remove(balloon)

    #### ---- SPAWN NEW SPRITES ---- ####

    # --- Spawn clouds --- #

    # E6: Increment the cloud_timer by c.get_time()

    cloud_timer += c.get_time()

    # E7: If cloud_timer is more than
    # time_between_clouds

    if cloud_timer > time_between_clouds:

        # E8: Create a random_index variable with a
        # random value between 0 and the length of
        # cloud_names - 1

        random_index = random.randint(0, len(cloud_names) - 1)

        # E9: Get the item from position random_index
        # in cloud_names and assign it to image

        image = cloud_names[random_index]
        

        # E10: Create a SPRITE called cloud using image,
        # at x 1020 and a random y between -10 and 550

        cloud = tsk.Sprite(image, 1020, random.randint(-10, 550))

        # E11: Append cloud to the list of clouds

        clouds.append(cloud)

        # E12: Set cloud_timer to 0
        # ---> TEST AFTER THIS LINE <--- #

        cloud_timer = 0

        # Q1: Decrement time_between_clouds by 50

        time_between_clouds -= 50

    # --- Spawn balloons --- #

    # K4: Increment balloon_timer by c.get_time()

    balloon_timer += c.get_time()

    # K5: If balloon_timer is more than
    # time_between balloons

    if balloon_timer > time_between_balloons:

        # K6: Create a new SPRITE called balloon at
        # 1020 x and a random y between 50 and 500,
        # using image "Balloon.png"

        balloon = tsk.Sprite("Balloon.png", 1020, random.randint(50, 500))

        # K7: Append balloon to the balloons list

        balloons.append(balloon)

        # K8: Set balloon_timer to 0
        # ---> TEST AFTER THIS LINE <--- #

        balloon_timer = 0


    #### ---- STOP FLAME ---- ####

    # J3: If flame_on

    if flame_on:

        # J4: Increment flame_timer by c.get_time()

        flame_timer += c.get_time()

        # J5: If flame_timer is greater than or equal
        # to flame_duration

        if flame_timer >= flame_duration:

            # J6: Set flame_on to False

            flame_on = False

            # J7: Set flame_timer to 0

            flame_timer = 0

            # J8: Set flame's CENTER_Y to -100
            # ---> TEST AFTER THIS LINE <--- #

            flame.center_y = -100

    #### --- SCROLL SCREEN --- ####

    # --- Background --- #

    # C2: Decrement the background's CENTER_X by .1
    # * c.get_time()

    background.center_x -= 0.1 * c.get_time()

    # C3: If the background's CENTER_X is less than or
    # equal to 0

    if background.center_x <= 0:

        # C4: Set the background's CENTER_X to 1018

        background.center_x = 1018

    # --- Clouds --- #

    # F2: For each cloud in the list of clouds

    for cloud in clouds:

        # F3: Decrement the cloud's CENTER_X by
        # cloud_move_speed * c.get_time()

        cloud.center_x -= cloud_move_speed * c.get_time()
    

    # --- Balloons --- #

    # L2: For each balloon in the balloons list

    for balloon in balloons:

        # L3: Decrement the balloon's CENTER_X by
        # balloon_move_speed * c.get_time()

        balloon.center_x -= balloon_move_speed * c.get_time()

    #### ---- REMOVE OFF-SCREEN SPRITES ---- ####

     # --- Clouds --- #

    # G1: Create an empty list called old_clouds

    old_clouds = []

    # G2: For each cloud in the clouds list

    for cloud in clouds:

        # G3: If the cloud's CENTER_X is less than -100

        if cloud.center_x < -100:

            # G4: Append cloud to the old_clouds list

            old_clouds.append(cloud)

    # G5: For each cloud in the old_clouds list

    for cloud in old_clouds:

        # G6: Remove cloud from the clouds list
        # ---> TEST AFTER THIS LINE <--- #

        clouds.remove(cloud)

    # --- Balloons --- #

    # M1: Create an empty list called old_balloons

    old_balloons = []

    # M2: For each balloon in the list of balloons

    for balloon in balloons:

        # M3: If the balloon's CENTER_X is less than
        # -100

        if balloon.center_x < -100:

            # M4: Append the balloon to old_balloons

            old_balloons.append(balloon)

    # M5: For each balloon in old_balloons

    for balloon in old_balloons:
    
        # M6: Remove the balloon from the balloons list
        # ---> TEST AFTER THIS LINE <--- #

        balloons.remove(balloon)

    #### ---- DRAW FRAME ---- ####

    # B3: DRAW the background

    background.draw()

    # F4: For each cloud in the clouds list

    for cloud in clouds:

        # F5: DRAW the cloud
        # ---> TEST AFTER THIS LINE <--- #

        cloud.draw()

    # L4: For each balloon in the balloons list

    for balloon in balloons:

        # L5: DRAW the balloon
        # ---> TEST AFTER THIS LINE <--- #

        balloon.draw()

    # D8: UPDATE the dragon using c.get_time()

    dragon.update(c.get_time())

    # D9: DRAW the dragon
    # ---> TEST AFTER THIS LINE <--- #

    dragon.draw()

    # I7: UPDATE flame using c.get_time()

    flame.update(c.get_time())

    # I8: DRAW the flame
    # ---> TEST AFTER THIS LINE <--- #

    flame.draw()

    # B4: Flip the display
    # ---> TEST AFTER THIS LINE <--- #

    pygame.display.flip()


    #### ---- TIME & SCORE ---- ####

    # C5: Tick clock c with 30 framerate
    # ---> TEST AFTER THIS LINE <--- #

    c.tick(30)

    # O2: Increment distance by 1

    distance += 1

    # Q2: If the time_between_clouds is less than 750

    if time_between_clouds < 750:

        # Q3: Set time_between_clouds to 750
        # ---> TEST AFTER THIS LINE <--- #

        time_between_clouds = 750

#### ---- FINAL SCORE ---- ####

# O3: Print the distance / 100 typecast to a string as
# part of a message to the user
# ---> TEST AFTER THIS LINE <--- #


print("You traveled " + str(distance / 100) + " meters" + ",")

# P3: Print the score typecast to a string as part of a
# message to the user
# ---> TEST AFTER THIS LINE <--- #


print("And you popped " + str(score) + " balloons" + ".")





