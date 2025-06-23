#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()


#### --------------------------- ####
#### ---- RANDOM BACKGROUND ---- ####
#### --------------------------- ####
def random_background(bg):
    pictures = ["AlienSpace.jpg", "Hills.jpg", "SchoolHallway.jpg"]
    back = random.choice(pictures)
    bg.image = back
    return back
#    back = random.randint(1, 3)
#    if back == 1:
 #       bg.image = "AlienSpace.jpg"
#        return "AlienSpace.jpg"
#    elif back == 2:
 #       bg.image = "Hills.jpg"
  #      return "Hills.jpg"
   # elif back == 3:
    #    bg.image = "SchoolHallway.jpg"
     #   return "SchoolHallway.jpg"


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# Setup
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("Hills.jpg", 0, 0)

# Sprites
panda = tsk.Sprite("Panda.png", 100, 100)
rock = tsk.Sprite("BigMossyRock.png", 400, 20)
vase = tsk.Sprite("ShortVase.png", 670, 280)


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            back = random_background(background)
            #background.image = back
            print("The new background is: " + back)

    # Draw
    background.draw()
    rock.draw()
    panda.draw()
    vase.draw()
    pygame.display.flip()
