"""
LESSON: 5.1 - Sprites
WARMUP 4
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock() 

background = tsk.Sprite("LakeWithBushes.jpg", 0, 0)
bee = tsk.Sprite("Bee.png", 300, 200)

timer = 0
bee_speed = 5

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    timer += c.get_time()
    if timer > 2000:
        timer = 0

        # Flip bee and change and bee_speed here
        bee.flip_x = not bee.flip_x
        bee_speed *= -1
    


    bee.x += bee_speed

    background.draw()
    bee.draw()
    pygame.display.flip()

    c.tick(30)