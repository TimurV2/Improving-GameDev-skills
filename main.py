import pygame
from pygame import *
import tkinter as tk
from tkinter import *
root = tk.Tk()


screen_width = root.winfo_screenwidth()             # | Узнаём высоту и ширину экрана пользователя
screen_height = root.winfo_screenheight()           # |
screen_size = (screen_width, screen_height)


class GameOfLife:

    def __init__(self, complexity, x, y, speed):
        self.complexity = complexity               # Выбираем сложность и узнаём с установкой размер окна пользователя
        self.screen = pygame.display.set_mode(screen_size)
        self.x = x
        self.y = y
        self.speed = speed

    def screen(self):
        pass

    def run(self):

        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Выжить на сессии')
        running = True

        file = 'secret.ogg'                             #
        pygame.mixer.pre_init(44100, 32, 2, 4096)       #
        pygame.mixer.init()                             #
        pygame.mixer.music.load(file)                   # Настройка микшера для проигрывания, музыка ставится на паузу с помощью ПРОБЕЛА
        pygame.mixer.music.play(-1)                     #
        pygame.mixer.Sound(file)                        #
        flpause = False                                 #
        volume = 1                                      #

        while running:

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        flpause = not flpause
                        if flpause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                    elif event.key == pygame.K_1:               # Убавление звука на 1
                        volume = volume - 0.1
                        pygame.mixer.music.set_volume(volume)
                    elif event.key == pygame.K_2:               # Прибавление звука на 2
                        volume = volume + 0.1
                        pygame.mixer.music.set_volume(volume)

            pygame.display.update()
            back_ground_img = pygame.image.load('kosmos-art-hellsescapeartist-tylercreatesworlds.jpg')  # Ставим задний фон
            self.screen.blit(back_ground_img, (0, 0))
            self.movement()     # Вызываем функцию движения персонажа (пока что просто зелёный шар)

        pygame.quit()

    def movement(self):                 # Здесь прописано движение персонажа игрока с его прорисовкой

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        pygame.draw.circle(self.screen, pygame.Color("Green"), (self.x, self.y), 50)


if __name__ == '__main__':
    game = GameOfLife(3, 990, 220, 15)
    game.run()
