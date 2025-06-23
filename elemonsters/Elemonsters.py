#### ---- LIBRARIES ---- ####
import tsk
import random
import pygame
pygame.init()

#### --------------------- ####
#### ---- PLAYER WINS ---- ####
#### --------------------- ####
def player_wins(player_sprite, enemy_sprite):
    p = player_sprite.image
    e = enemy_sprite.image
    if p == "FireMonster.png" and e == "GrassMonster.png":
        win = True
    elif p == "GrassMonster.png" and e == "StoneMonster.png":
        win = True
    elif p == "StoneMonster.png" and e == "ElectricMonster.png":
        win = True
    elif p == "ElectricMonster.png" and e == "WaterMonster.png":
        win = True
    elif p == "WaterMonster.png" and e == "FireMonster.png":
        win = True

    return "Black.png"


#### --------------------------- ####
#### ---- GET_MONSTER_IMAGE ---- ####
#### --------------------------- ####

def get_monster_image(key_value):
    monsters = ["FireMonster.png", "GrassMonster.png", "StoneMonster.png", "ElectricMonster.png", "WaterMonster.png"]

    if key_value == -1:
        return random.choice(monsters)
    elif key_value == pygame.K_a:
        return monsters[0]
    elif key_value == pygame.K_s:
        return monsters[1]
    elif key_value == pygame.K_d:
        return monsters[2]
    elif key_value == pygame.K_f:
        return monsters[3]
    elif key_value == pygame.K_v:
        return monsters[4]
    else:
        return "Blank.png"


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# --- Setup --- #
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# --- Sprites --- #                                     
background = tsk.Sprite("Arena.jpg", 0, 0)
player = tsk.Sprite("Blank.png", 150, 200)
enemy = tsk.Sprite("Blank.png", 700, 200)

#### ---- RE-STRUCTURE 2 ---- ####

# Call the get_monster_image function you created and
# get a random monster image to assign to enemy.image

enemy.image = get_monster_image(-1)

#### ---- END RESTRUCTURE 2 ---- ####

enemy.flip_x = True

# --- Variables --- #
countdown = 3000
misses = 0
hits = 0
timer_bar = pygame.Rect(0, 550, 1018, 50)
move_increment = 1018 / countdown

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    #### ---- EVENT LOOP ---- ####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # --- Put up monster when user presses key --- #
        if event.type == pygame.KEYDOWN:

            #### ---- RE-STRUCTURE 1 ---- ####

            # Use the code below to write the function
            # get_moster_image that takes a key value
            # and returns the matching image from the
            # monsters list. If the key value is -1,
            # it returns a random monster. Call the
            # function here and assign the result to
            # player.image

            player.image = get_monster_image(event.key)
            
            #### ---- END RESTRUCTURE 1 ---- ####

    # --- Timer bar moves left --- #
    speed = move_increment * c.get_time()
    timer_bar.x -= int(speed)
    countdown -= c.get_time()

    # --- When timer runs down, compare monsters --- #
    if countdown <= 0:

        #### ---- RE-STRUCTURE 4 ---- ####

        # Use the code below to create a function
        # called player_wins that takes two sprites and
        # returns a boolean. Call the function here
        # and assign the result to the variable win.
        
        win = player_wins(player, enemy)

        #### ---- END RESTRUCTURE 4 ---- ####

        if win:
            hits += 1
        else:
            misses += 1

        #### ---- RE-STRUCTURE 3 ---- ####

        # Call the get_monster_image function you
        # created and get a random monster image to
        # assign to enemy.image
        enemy.image = get_monster_image(-1)
        countdown = 2000
        timer_bar.x = 0

        #### ---- END RESTRUCTURE 3 ---- ####

        countdown = 2000
        timer_bar.x = 0


    #### ---- DRAW ---- ####

    # --- Scene --- #
    background.draw()
    player.draw()
    enemy.draw()

    # --- Interface --- #
    for i in range(hits):
        pygame.draw.circle(w, (0, 0, 255), (100 + i * 50, 50), 20)

    for i in range(misses):
        pygame.draw.circle(w, (255, 0, 0), (600 + i * 50, 50), 20)

    pygame.draw.rect(w, (0, 255, 0), timer_bar)

    # --- Finish --- #
    countdown -= c.get_time()
    pygame.display.flip()
    c.tick(30)

    # --- Scores --- #
    if hits >= 5 or misses >= 5:
        drawing = False
        print("FINAL SCORE")
        print("---------------")
        print("Wins: " + str(hits))
        print("Losses: " + str(misses))


# Turn in your Coding Exercise.
