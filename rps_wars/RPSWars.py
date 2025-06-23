"""
LESSON: RPS Wars Project
"""

#### ---- LIBRARIES ---- ####

# D1: Import the random library

import random

# B1: Import the tsk library

import tsk

# A1: Import the pygame library

import pygame

# A2: Initialize pygame

pygame.init()

#### ----------------------------------- ####
#### ---- D7: SPAWN SPRITE FUNCTION ---- ####
#### ----------------------------------- ####

# DEFINE spawn_sprite function with PARAMETERS
# sprite_list and DEFAULT PARAMETER key with value -1

def spawn_sprite(sprite_list, key = -1):

    # Create a list called images with filename strings
    # RPSRock.png, RPSPaper.png, and RPSScissors.png

    images = ["RPSRock.png", "RPSPaper.png", "RPSScissors.png"]

    # --- Decide which image will be spawned --- #

    # If key is -1

    if key == -1:

        # Make a random CHOICE from the images list and
        # assign it to image

        image = random.choice(images)

    # Else if key is the key constant for the "a" key

    elif key == pygame.K_a:

        # Assign image the value at index 0 in images

        image = images[0]

    # Else if key is the key constant for the "s" key

    elif key == pygame.K_s:

        # Assign image the value at index 1 in images

        image = images[1]

    # Else if key is the key constant for the "d" key

    elif key == pygame.K_d:

        # Assign image the value at index 2 in images

        image = images[2]

    # Else

    else:

        # RETURN

        return

    # --- Spawn on the appropriate side --- #

    # If key is -1

    if key == -1:

        # Assign sprite a new Sprite object using image
        # at position 800, 300

        sprite = tsk.Sprite(image, 800, 300)

        # Set the sprite's flip_x to True

        sprite.flip_x = True

    # Else

    else:

        # Assign sprite a new Sprite object using image
        # at position 100, 300

        sprite = tsk.Sprite(image, 100, 300)

    # Append sprite to sprite_list

    sprite_list.append(sprite)

#### -------------------------------------- ####
#### ---- G2: COLLIDE SPRITES FUNCTION ---- ####
#### -------------------------------------- ####

# DEFINE collide_sprites function with PARAMETERS good
# and bad

def collide_sprites(good, bad):

    # Create an empty list called dead_good_guys

    dead_good_guys = []

    # Create an empty list called dead_bad_guys

    dead_bad_guys = []

    # --- Check for collisions --- #

    # For each good_guy in good

    for good_guy in good:

        # For each bad_guy in bad

        for bad_guy in bad:

            # Assign win the result of CALLing
            # check_win with good_guy and bad_guy

            win = check_win(good_guy, bad_guy)

            # If win is greater than 0

            if win > 0:

                # Append bad_guy to the list
                # dead_bad_guys

                dead_bad_guys.append(bad_guy)

            # Else if win is less than 0

            elif win < 0:

                # Append good_guy to the list
                # dead_good_guys

                dead_good_guys.append(good_guy)

    # --- Remove dead sprites --- #

    # For each sprite in dead_good_guys

    for sprite in dead_good_guys:

        # Remove sprite from the good list

        good.remove(sprite)

    # For each sprite in dead_bad_guys

    for sprite in dead_bad_guys:

        # Remove sprite from the bad list

        bad.remove(sprite)

#### ------------------------------------ ####
#### ---- H2: GAME CONTINUE FUNCTION ---- ####
#### ------------------------------------ ####

# DEFINE the game_continue function with PARAMETERS
# good and bad

def game_continue(good, bad):

    # If length of good is more than 0

    if len(good) > 0:

        # If the object at index [0] in good has
        # center_x greater than 968

        if good[0].center_x > 968:

            # Print "You win!"

            print("You win! ")

            # RETURN False

            return False

    # If length of bad is more than 0

    if len(bad) > 0:

        # If the object at index [0] in bad has
        # center_x less than 50

        if bad[0].center_x < 50:

            # Print "Sorry, you lose."

            print("Sorry, you lose. ")

            # RETURN False

            return False

    # RETURN True
    # ---> TEST AFTER THIS LINE <--- #

    return True

#### -------------------------------- ####
#### ---- G3: CHECK WIN FUNCTION ---- ####
#### -------------------------------- ####

# DEFINE function check_win with PARAMETERS good and
# bad

def check_win(good, bad):

    # If good and bad are not colliding, or their
    # images are the same

    if not pygame.sprite.collide_rect(good, bad) or good.image == bad.image:


        # RETURN 0

        return 0

    # --- Win conditions --- #

    # Assign r_beats_s the result of whether good's
    # image is equal to "RPSRock.png" and bad's image
    # is equal to "RPSScissors.png"

    r_beats_s = good.image == "RPSRock.png" and bad.image == "RPSScissors.png"

    # Assign s_beats_p the result of whether good's
    # image is equal to "RPSScissors.png" and bad's
    # image is equal to "RPSPaper.png"

    s_beats_p = good.image == "RPSScissors.png" and bad.image == "RPSPaper.png"

    # Assign p_beats_r the result of whether good's
    # image is "RPSPaper.png" and bad's image is
    # "RPSRock.png"

    p_beats_r = good.image == "RPSPaper.png" and bad.image == "RPSRock.png"

    # If r_beats_s or s_beats_p or p_beats_r

    if r_beats_s or s_beats_p or p_beats_r:

        # RETURN 1

        return 1

    # --- Lose condition --- #

    # Otherwise

    else:

        # RETURN -1
        # ---> TEST AFTER THIS LINE <--- #

        return -1

#### ------------------------------------ ####
#### ---- I5: DRAW TRIANGLE FUNCTION ---- ####
#### ------------------------------------ ####

# DEFINE the draw_triangle function with PARAMETERS
# window, position, and color

def draw_triangle(window, position, color):

    # Assign x, y the value position

    x, y = position

    # Assign y_top the value y + 50

    y_top = y + 50

    # Assign y_bottom the value y + 100

    y_bottom = y + 100

    # Assign x_left the value x - 25

    x_left = x - 25

    # Assign x_right the value x + 25

    x_right = x + 25

    # Draw a polygon in window with color, connecting
    # points (x_left, y_bottom), (x, y_top), and
    # (x_right, y_bottom)
    # ---> TEST AFTER THIS LINE <--- #

    pygame.draw.polygon(window, color, [(x_left, y_bottom), (x, y_top), (x_right, y_bottom)])

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

#### ---- SETUP ---- ####

# A3: Assign w a window of size 1018 x 573

w = pygame.display.set_mode([1018, 573])

# C1: Assign c a new Clock

c = pygame.time.Clock()

# B2: Assign background a Sprite using "TowerSiege.jpg"
# at position 0, 0

background = tsk.Sprite("TowerSiege.jpg", 0, 0)

# --- Variables --- #

# C2: Set player_spawn_timer to 0

player_spawn_timer = 0

# C3: Set enemy_spawn_timer to 0

enemy_spawn_timer = 0

# D2: Set allies to an empty list

allies = []

# E1: Set enemies to an empty list

enemies = []

#### ---- MAIN LOOP ---- ####

# A4: Set drawing to True

drawing = True

# A5: Set playing to True

playing = True

# A6: Loop while drawing and playing

while drawing and playing:

    # --- Event loop --- #

    # A7: Start an event loop

    for event in pygame.event.get():

        # A8: If the event type is QUIT

        if event.type == pygame.QUIT:

            # A9: Set drawing to False
            # ---> TEST AFTER THIS LINE <--- #

            drawing = False

        # D3: If the event type is KEYDOWN

        if event.type == pygame.KEYDOWN:

            # D4: If player_spawn_timer is more than 1000

            if player_spawn_timer > 1000:

                # D5: Set player_spawn_timer to 0

                player_spawn_timer = 0

                # D6: CALL spawn_sprite with ARGUMENTS
                # allies and event.key

                spawn_sprite(allies, event.key)


    #### ---- BEHAVIOR --- ####

    # --- Spawn new enemies --- #

    # E2: If enemy_spawn_timer is 1500 or more

    if enemy_spawn_timer >= 1500:

        # E3: Set enemy_spawn_timer to 0

        enemy_spawn_timer = 0

        # E4: CALL spawn_sprite with ARGUMENT enemies

        spawn_sprite(enemies)

    # --- Move --- #

    # F1: For each sprite in allies

    for sprite in allies:

        # F2: Increment the sprite's x by .1 * c.get_time()

        sprite.x += 0.1 * c.get_time()

    # F3: For each sprite in enemies

    for sprite in enemies:

        # F4: Decrement the sprite's x by .1 * c.get_time()
        # ---> TEST AFTER THIS LINE <--- #

        sprite.x -= 0.1 * c.get_time()

    # --- Check for wins and losses --- #

    # G1: CALL collide_sprites with allies and enemies

    collide_sprites(allies, enemies)

    # H1: CALL game_continue with allies and enemies
    # and assign the result to playing

    playing = game_continue(allies, enemies)

    #### ---- DRAWING ---- ####

    # --- Draw scene --- #

    # B3: Draw the background

    background.draw()

    # E5: For each sprite in enemies

    for sprite in enemies:

        # E6: Draw the sprite
        # ---> TEST AFTER THIS LINE <--- #

        sprite.draw()

    # D8: For each sprite in allies

    for sprite in allies:

        # D9: Draw the sprite
        # ---> TEST AFTER THIS LINE <--- #

        sprite.draw()

    # --- Draw tracking triangles --- #

    # I1: If the length of enemies is greater than 0

    if len(enemies) > 0:

        # I2: CALL draw_triangle with ARGUMENTS w, the
        # center of the sprite at enemies[0], and the
        # color red

        draw_triangle(w, enemies[0].center, color = (255, 0, 0))

    # I3: If the length of allies is greater than 0

    if len(allies) > 0:

        # I4: CALL draw_triangle with ARGUMENTS w, the
        # center of the sprite allies[0], and the
        # color green

        draw_triangle(w, allies[0].center, color = (0, 255, 0))


    # --- End --- #

    # C4: Tick clock c with framerate 30

    c.tick(30)

    # B4: Flip the display
    # ---> TEST AFTER THIS LINE <--- #

    pygame.display.flip()

    # C5: Increment player_spawn_timer by c.get_time()

    player_spawn_timer += c.get_time()
 
    # C6: Increment enemy_spawn_timer by c.get_time()
    # ---> TEST AFTER THIS LINE <--- #

    enemy_spawn_timer += c.get_time()
