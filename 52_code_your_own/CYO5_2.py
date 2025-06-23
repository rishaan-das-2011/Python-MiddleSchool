"""
LESSON: 5.2 - Spritesheet Animation
EXERCISE: Code Your Own

TITLE: Hedgehog In The City
DESCRIPTION: This is a simple PyGame Code where once the kernel is ran, a hedgehog
in a City Pasture appear. When you click the mouse, the hedgehog pauses or resumes
its running animation. Pressing the spacebar makes the hedgehog move steadily to 
the right across the screen. The program lets you control animations and 
movement using mouse clicks and keyboard inputs.
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("AirCityPasture.jpg", 0, 0)
HedgeHogRunSheet = tsk.ImageSheet("HedgehogRunSheet.png", 5, 6)
hedgehog = tsk.Sprite(HedgeHogRunSheet, 300, 250)
hedgehog.image_animation_rate = 30  # Base animation rate

timer = 0
slow_time = 80  # Time interval in milliseconds for slowing down

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

    # Check for space bar press every frame
    if tsk.get_key_pressed(pygame.K_SPACE):
        print("Moving right!")
        hedgehog.x += 0.5 * c.get_time()

    # Update timer
    timer += c.get_time()


    # Draw and update
    background.draw()
    hedgehog.draw()
    hedgehog.update(c.get_time())

    pygame.display.flip()
    c.tick(30)

# Turn in your Coding Exercise.
