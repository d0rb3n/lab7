import pygame
import os

pygame.init()
screen = pygame.display.set_mode((850, 400), pygame.RESIZABLE)
pygame.display.set_caption("d0rbMusic")
pygame.display.set_icon(pygame.image.load("icon.png"))
vol = 0.3
pygame.mixer.music.set_volume(vol)


def change_volume(vol):
    pygame.mixer.music.set_volume(vol)

def play(music):
    print("Playing track:", music)
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def nexttrack():
    global current_song
    current_song = (current_song + 1) % len(playlist)
    play(playlist[current_song])

def prevtrack():
    global current_song
    current_song = (current_song - 1) % len(playlist)
    play(playlist[current_song])

playlist = ['Goosebumps.mp3', '5%TNT.mp3', 'HighestInTheRoom.mp3', 'ButterflyEffect.mp3']
current_song = 0

playing = True
paused = False

while playing: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit() 
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_SPACE: 
                if paused: 
                    unpause() 
                    paused = False 
                else: 
                    pause() 
                    paused = True 
            elif event.key == pygame.K_s: 
                if pygame.mixer.music.get_busy(): 
                    unpause() 
                    paused = False 
                else: 
                    play(playlist[current_song]) 
            elif event.key == pygame.K_RIGHT: 
                nexttrack() 
            elif event.key == pygame.K_LEFT: 
                prevtrack() 

    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text1 = font.render('Press S to Start',True, (255, 255, 255))
    text2 = font.render('Press SPACE to pause/play',True, (255, 255, 255))
    text3 = font.render('Press Right arrow for next song',True, (255, 255, 255))
    text4 = font.render('Press Left arrow for next song', True, (255, 255, 255))                                   
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 50))
    screen.blit(text3, (10, 90))
    screen.blit(text4, (10, 130))
    pygame.display.flip()

pygame.quit()
