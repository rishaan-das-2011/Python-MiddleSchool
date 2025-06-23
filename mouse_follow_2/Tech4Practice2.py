"""
LESSON: 5.1 - Sprites
TECHNIQUE 4: Mouse Follow
PRACTICE 2
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])

background = tsk.Sprite("OutdoorHills.jpg", 0, 0)
hedgehog = tsk.Sprite("HedgehogRunPose.png", 260, 220)

following = False

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            following = True
        if event.type == pygame.MOUSEBUTTONUP:
            following = False
            
    if following:   
        x, y = pygame.mouse.get_pos()
        hedgehog.center = (x, y)
            
            




    background.draw()
    hedgehog.draw()
    pygame.display.flip()


# Turn in your Coding Exercise.
