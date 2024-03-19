import pygame
import sys

pygame.init()

s_width = 700
s_height = 600
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("RedBall")
clock = pygame.time.Clock()
FPS = 30

ball = (255, 0, 0)

radius = 25
x = s_width // 2
y = s_height // 2

pixels = 20

flLeft = flRight = flUP = flDOWN = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            elif event.key == pygame.K_UP:
                flUP = True
            elif event.key == pygame.K_DOWN:
                flDOWN = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                flLeft = flRight = flUP = flDOWN = False
    if flLeft and x - pixels >= pixels:
        x -= pixels
    elif flRight and x <= s_width - 2*pixels:
        x += pixels
    if flUP and y - pixels >= radius:
        y -= pixels
    elif flDOWN and y <= s_height - 2*radius:
        y += pixels


    screen.fill((255, 255, 255))    
    pygame.draw.circle(screen, ball, (x, y), radius)
    pygame.display.flip()
    clock.tick(FPS)