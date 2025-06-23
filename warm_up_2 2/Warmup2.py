"""
LESSON: 5.3 - Sprite Collision
WARMUP 2
"""

import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("LivingRoom.jpg", 0, 0)
ball = tsk.Sprite("TennisBall.png", 0, 0)
vases = [tsk.Sprite("BushVase1.png", 250, 400), tsk.Sprite("BushVase2.png", 350, -100), tsk.Sprite("BushVase3.png", 500, 400)]

ball_x_speed = 0.15
ball_y_speed = 0.18

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Move ball here

    ball.center_x += ball_x_speed * c.get_time()
    ball.center_y += ball_y_speed * c.get_time()


    # Collision with vases here

    for vase in vases:
        if pygame.sprite.collide_rect(ball, vase):
            ball_x_speed *= -1
            ball_y_speed *= -1


    if ball.center_x >= 1018 or ball.center_y >= 573 or ball.center_y <= 0:
        drawing = False

    background.draw()
    for vase in vases:
        vase.draw()
    ball.draw()
    pygame.display.flip()

    c.tick(30)