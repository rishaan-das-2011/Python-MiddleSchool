"""
LESSON: 6.3 - Complex Parameters
TECHNIQUE 2: Default Parameters
PRACTICE 2
"""

#### ---- LIBRARIES ---- ####
import tsk
import pygame
pygame.init()


#### ---------------------------- ####
#### ---- SPIN BALL FUNCTION ---- ####
#### ---------------------------- ####
def spin_ball(ball, clock, ball_speed = 0.1):                 
    speed = ball_speed * clock.get_time()
    ball.angle -= speed

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Arena.jpg", 0, 0)
soccer_ball = tsk.Sprite("SoccerBall.png", 160, 250)
tennis_ball = tsk.Sprite("TennisBall.png", 460, 350)
other_ball = tsk.Sprite("Ball.png", 760, 250)


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
 
    # Spin balls
    spin_ball(soccer_ball, c)                       
    spin_ball(other_ball, c)                        

    # If necessary, spin other ball faster
    if tsk.is_key_down(pygame.K_SPACE):
        spin_ball(tennis_ball, c, .5)
    else:
        spin_ball(tennis_ball, c)                   

    # Draw
    background.draw()
    soccer_ball.draw()
    tennis_ball.draw()
    other_ball.draw()

    # Finish
    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
