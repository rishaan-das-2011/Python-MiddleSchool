"""
LESSON: 5.2 - Sprite Sheet Animation
WARMUP 3
"""
import pygame
import tsk
import random
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("LakeWithBushes.jpg", 0, 0)
run_sheet = tsk.ImageSheet("HedgehogRun.png", 5, 6)
hedgehog = tsk.Sprite(run_sheet, 300, 200)
hedgehog.image_animation_rate = 30

timer = 0
time_up = 2000
running = True

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    timer += c.get_time()
    if timer > time_up:
        timer = 0
        time_up = random.randint(1500, 3000)
        running = not running

        hedgehog.image_animation_rate = 30 if running else 0


    background.draw()

    # Update and draw the hedgehog
    hedgehog.update(c.get_time())
    hedgehog.draw()



    pygame.display.flip()
    c.tick(30)