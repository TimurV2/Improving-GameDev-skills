import pygame
from pygame import *
import tkinter as tk
from tkinter import *
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_size = (screen_width, screen_height)


class GameOfLife:
    x, y = 990, 220
    speed = 15

    def __init__(self, complexity):
        self.complexity = complexity               #Выбираем сложность и узнаём с установкой размер окна пользователя
        self.screen = pygame.display.set_mode(screen_size)

    def screen(self):
        pass

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Выжить на сессии')
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            #тестим правильную работу программы
            back_ground_img = pygame.image.load('kosmos-art-hellsescapeartist-tylercreatesworlds.jpg')
            self.screen.blit(back_ground_img, (0, 0))
            if pygame.key.get_pressed():
                self.movement()
        pygame.quit()

    def movement(self):
        x = screen_height / 2
        y = screen_width / 2
        speed = 15
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed



if __name__ == '__main__':
    game = GameOfLife(3)
    game.run()
