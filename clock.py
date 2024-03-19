import pygame
import math 
 
pygame.init() 
 
screen = pygame.display.set_mode((900,900), pygame.RESIZABLE) 
 
clock = pygame.image.load('main-clock.png') 
clock_rect = clock.get_rect(center=(900 // 2, 900 // 2)) 
minute = pygame.image.load('right-hand.png') 
second = pygame.image.load('left-hand.png') 
 
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 
    current_time = pygame.time.get_ticks() 

    seconds = current_time // 1000 % 60 
    minutes = current_time // 60000 % 60

    sec_angle = -math.radians(seconds * 6) + math.pi / 2
    min_angle = -math.radians(minutes * 6) + math.pi / 2

    turn_minute = pygame.transform.rotate(minute, math.degrees(min_angle)) 
    turn_second = pygame.transform.rotate(second, math.degrees(sec_angle))

    minute_rect = turn_minute.get_rect(center=clock_rect.center) 
    second_rect = turn_second.get_rect(center=clock_rect.center) 

    screen.fill((255,255,255)) 
    screen.blit(clock, clock_rect)
    screen.blit(turn_minute, minute_rect) 
    screen.blit(turn_second, second_rect) 
 
    pygame.display.flip()