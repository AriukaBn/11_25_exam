import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('asdf')
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

fps = 60
ballx = 400
bally = 300
ballr = 30
vx = 5
vy = 5

ball2x = 200
ball2y = 150
ball2r = 40
v2x = 10
v2y = 10

ball3x = 600
ball3y = 450
ball3r = 50
v3x = 15
v3y = 15

running = True

while running:
# Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ballx += vx
    bally += vy
    if(ballx-ballr<=0 or ballx+ballr>=800):
        vx = -vx
    if(bally-ballr<=0 or bally+ballr>=600):
        vy = -vy
    screen.fill(black)
    pygame.draw.circle(screen, red, (ballx,bally), ballr)

    ball2x += v2x
    ball2y += v2y
    if(ball2x-ball2r<=0 or ball2x+ball2r>=800):
        v2x = -v2x
    if(ball2y-ball2r<=0 or ball2y+ball2r>=600):
        v2y = -v2y
    pygame.draw.circle(screen, green, (ball2x,ball2y), ball2r)

    ball3x += v3x
    ball3y += v3y
    if(ball3x-ball3r<=0 or ball3x+ball3r>=800):
        v3x = -v3x
    if(ball3y-ball3r<=0 or ball3y+ball3r>=600):
        v3y = -v3y
    pygame.draw.circle(screen, blue, (ball3x,ball3y), ball3r)
    


    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
sys.exit()