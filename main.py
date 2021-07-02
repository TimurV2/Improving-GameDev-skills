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
        flpause = False
        clock = pygame.time.Clock()
        pygame.display.set_caption('Выжить на сессии')
        running = True
        pygame.mixer.init(44100, 16, 2, 4096)
        pygame.mixer.music.load('DOOM.mp3')
        pygame.mixer.music.play(-1)
        while running:

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if event.key == pygame.K_SPACE:
                flpause = not flpause
                if flpause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            pygame.display.update()
            back_ground_img = pygame.image.load('kosmos-art-hellsescapeartist-tylercreatesworlds.jpg')
            self.screen.blit(back_ground_img, (0, 0))
            self.movement()
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
