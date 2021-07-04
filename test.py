import pygame
import sys

sc = pygame.display.set_mode((400, 300))
pygame.init()
pygame.mixer.music.load('secret.ogg')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()
pygame.mixer.pre_init(44100, 32, 2, 4096)
pygame.mixer.init()

flpause = True
volume = 1

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                flpause = not flpause
                if flpause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif i.key == pygame.K_1:
                volume = volume - 0.1
                pygame.mixer.music.set_volume(volume)
            elif i.key == pygame.K_2:
                volume = volume + 0.1
                pygame.mixer.music.set_volume(volume)
