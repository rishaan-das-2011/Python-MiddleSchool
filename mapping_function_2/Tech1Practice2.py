"""
LESSON: 6.2 - Return Values
TECHNIQUE 1: Mapping Function
PRACTICE 2
"""

#### ---- LIBRARIES ---- ####
import tsk
import pygame
pygame.init()


#### --------------------------- ####
#### ---- GET NAME FUNCTION ---- ####
#### --------------------------- ####
def get_name(imageName):
    if imageName == "PandaPilot.png":
        return "Panda Pilot"
    elif imageName == "Panda.png":
        return "Normal Panda"
    elif imageName == "PandaDuck.png":
        return "Panda Duck"
    elif imageName == "PandaGentleman.png":
        return "Panda Gentleman"
    elif imageName == "PandaPilot.png":
        return "Panda Pilot"



#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# Setup
w = pygame.display.set_mode([1018, 573])

# Sprites
background = tsk.Sprite("LivingRoom.jpg", 0, 0)
panda1 = tsk.Sprite("Panda.png", 600, 0)
panda2 = tsk.Sprite("PandaDuck.png", 100, 0)
panda3 = tsk.Sprite("PandaGentleman.png", 700, 200)
panda4 = tsk.Sprite("PandaPilot.png", 0, 200)

panda1.flip_x = True
panda3.flip_x = True

all_pandas = [panda1, panda2, panda3, panda4]


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # Uncomment this section once the function
            # is finished
            for panda in all_pandas:
                if panda.rect.collidepoint(x, y):
                    name = get_name(panda.image)
                    print("You clicked the " + str(name))

    # Draw
    background.draw()
    for panda in all_pandas:
        panda.draw()

    # Finish
    pygame.display.flip()


# Turn in your Coding Exercise.
