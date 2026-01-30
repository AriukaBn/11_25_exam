import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption('asdf')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)


running = True

while running:
# Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(blue)

    pygame.draw.rect(screen, red, (100,100,250,100))


    pygame.display.flip()
pygame.quit()
sys.exit()