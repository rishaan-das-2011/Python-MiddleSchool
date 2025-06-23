"""
LESSON: 5.4 - Sprites in Lists
EXERCISE: Cat Traffic
"""

#### ---- SET UP ---- ####

# --- Libraries --- #
import tsk
import pygame
import random
pygame.init()


# --- Display Variables --- #
window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

floor = tsk.Sprite("CatRoom.jpg", 0, 0)
v_cat_speed = 0.06
h_cat_speed = 0.1
timer = 0



# --- Create cats --- #

cats = []
vertical_cats = []

kitten = tsk.Sprite("BoredCat.png", 30, 250)
cats.append(kitten)


#### ---- RE-STRUCTURE 1 ---- ####

# For i in range 3, create an x value that is 100 +
# 300 * i. Create new cat sprite using "GentleCat.png"
# at that x and height 50, then append it to the
# vertical_cats and cats lists.

for i in range (3):
    x = 100 + 300 * i
    cat = tsk.Sprite("GentleCat.png", x, 50)
    vertical_cats.append(cat)
    cats.append(cat)


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False


    #### --- MOVE CATS --- ####

    # --- Gentlemen Cats --- #

    #### ---- RE-STRUCTURE 2 ---- ####

    # Instead of doing this sequence 3 times with
    # 3 cats, do it as part of a for-each loop on the
    # list of vertical_cats

    at_edge = False

    for cat in vertical_cats:
        if not pygame.sprite.collide_rect(cat, kitten):
            cat.center_y += v_cat_speed * c.get_time()
            
    
        if cat.center_y > 573:
            cat.center_y = 573
            at_edge = True
        if cat.center_y < 150:
            cat.center_y = 150
            at_edge = True
            
    if at_edge:
        v_cat_speed *= -1

    # --- Kitten --- #

    direction = 1
    if h_cat_speed < 0:
        direction = -1

    if timer >= 1000:
        h_cat_speed = random.randint(5, 20) * .01 * direction
        timer = 0

    kitten.center_x += h_cat_speed * c.get_time()

    if kitten.center_x > 1018:
        kitten.center_x = 1018
        h_cat_speed *= -1

    if kitten.center_x < 0:
       kitten.center_x = 0
       h_cat_speed *= -1

    if h_cat_speed > 0:
        kitten.flip_x = False
    else:
        kitten.flip_x = True


    #### ---- DRAW CATS ---- ####

    # --- Order cat list by height --- #
    cats_by_height = []
    while len(cats) > 0:

        min = 2000
        lowest_cat = ""

        for cat in cats:
            if cat.center_y < min:
                min = cat.center_y
                lowest_cat = cat

        cats.remove(lowest_cat)
        cats_by_height.append(lowest_cat)

    cats = cats_by_height


    # --- Draw --- #
    floor.draw()

    #### ---- RE-STRUCTURE 3 ---- ####

    # For each cat in the cats list, draw that cat

    for cat in cats:
        cat.draw()

    # FLIP the display
    pygame.display.flip()

    # TICK the clock at 30 FPS
    c.tick(30)
    timer += c.get_time()


# Turn in your Coding Exercise.
