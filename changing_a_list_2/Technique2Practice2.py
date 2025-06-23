"""
LESSON: 4.1 - Lists
TECHNIQUE 2: Changing a List
PRACTICE 2
"""

# --- Setup --- #
import pygame
pygame.init()
window = pygame.display.set_mode([300, 300])
c = pygame.time.Clock()

keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

print("Hit all the keys (1-9) as quickly as you can!")

start_time = pygame.time.get_ticks()

# --- Main loop --- #
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # --- User guesses --- #
        if event.type == pygame.KEYDOWN:

            # If the event key is in keys, remove it
            if event.key in keys:
                keys.remove(event.key)
                
                 


            # Otherwise, print message and end program

            else:
                print("Session completed. If you didn't get a report of your time, you didn't hit the 1-9 keys correctly.")
                drawing = False



    # --- End the program --- #
    if len(keys) == 0:
        end_time = pygame.time.get_ticks()
        duration = (end_time - start_time) / 1000
        print("You hit all the keys in " + str(duration) + " seconds.")
        drawing = False

    # --- Draw --- #
    window.fill((0, 30, 60))
    c.tick(30)
    pygame.display.flip()


# Turn in your Coding Exercise.
