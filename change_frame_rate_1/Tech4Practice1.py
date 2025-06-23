"""
LESSON: 5.2 - Spritesheet Animation
TECHNIQUE 4: Changing Frame Rates
PRACTICE 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Fixed quotes and image loading
background = tsk.Sprite("OutdoorBushes.jpg", 0, 0)
image_sheet = tsk.ImageSheet("HedgehogRun.png", 5, 6)
hedgehog = tsk.Sprite(image_sheet, 300, 250)
hedgehog.image_animation_rate = 30

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:            
            if hedgehog.image_animation_rate == 0:
                hedgehog.image_animation_rate = 30 
                print("Resuming animation!")
            else:
                hedgehog.image_animation_rate = 0
                print("Pausing animation!")

    # Update and draw
    background.draw()
    hedgehog.draw()
    hedgehog.update(c.get_time())

    c.tick(30)
    pygame.display.flip()
    
    
    
# Turn in your Coding Exercise.
