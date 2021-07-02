import pygame
from pygame import *
file = 'DOOM.mp3'
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init(44100, 16, 2, 4096)
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
