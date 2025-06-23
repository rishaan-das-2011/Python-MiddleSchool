"""
LESSON: 5.3 - Sprite Collision
TECHNIQUE 3: Sprite Walls
DEMO 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Grass.jpg", 0, 0)
ball = tsk.Sprite("GolfBall.png", 50, 250)
bush = tsk.Sprite("BushesRight.png", 600, 350)
ant = tsk.Sprite("antblue.png", 0, 373)
ant.scale = .5 

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    x, y = pygame.mouse.get_pos()
    

    ## GOLF BALL ##
    old_center = ball.center  # old_center is the position the ball was in on the previous frame   
    ball.center = x, y
    
    # Check if ball collides with bush
    if pygame.sprite.collide_rect(ball, bush):
        ball.center = old_center

    ## ANT ##
    ant.center_x += .1 * c.get_time()

    # Check if ant collides with bush
    if pygame.sprite.collide_rect(ant, bush):
        ant.center_x -= .1 * c.get_time()


    background.draw()
    bush.draw()
    ant.draw()
    ball.draw()

    pygame.display.flip()
    c.tick(30)