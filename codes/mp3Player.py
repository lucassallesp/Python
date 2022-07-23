#Esse programa toca música no MP3 player.

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('not_today.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass

