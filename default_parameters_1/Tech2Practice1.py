"""
LESSON: 6.3 - Complex Parameters
TECHNIQUE 2: Default Parameters
PRACTICE 1
"""

#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()


#### ----------------------------- ####
#### ---- NEW SPRITE FUNCTION ---- ####
#### ----------------------------- ####
def new_sprite(all_sprites, image = "SmallBrownRock.png"):                     
    x = random.randint(20, 950)
    y = random.randint(100, 400)

    sprite = tsk.Sprite(image, x, y)
    all_sprites.append(sprite)


#### ---------------------------- ####
#### ---- FIND ROCK FUNCTION ---- ####
#### ---------------------------- ####
def find_rock(all_sprites):
    for sprite in all_sprites:
        if sprite.image == "SmallBrownRock.png":
            return sprite

    return -1


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Desert.jpg", 0, 0)
sprite_list = [background]
possible_keys = [pygame.K_x, pygame.K_t, pygame.K_b, pygame.K_q, pygame.K_w, pygame.K_z, pygame.K_y, pygame.K_l]
hidden_key = random.choice(possible_keys)
remove_rock_timer = 2000

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # Key presses
        elif event.type == pygame.KEYDOWN:

            # Correct key
            if event.key == hidden_key:
                new_sprite(sprite_list, "RoundGemBlue.png")
                hidden_key = random.choice(possible_keys)

            # All incorrect keys
            else:
                new_sprite(sprite_list) 

    # Remove one of the rocks every 2 seconds
    if remove_rock_timer <= 0:
        remove_rock_timer = 2000
        first_rock = find_rock(sprite_list)
        if first_rock != -1:
            sprite_list.remove(first_rock)

    # Draw
    for sprite in sprite_list:
        sprite.draw()

    # Finish
    remove_rock_timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
