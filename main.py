import pygame
from pygame import *
import tkinter as tk
from tkinter import *
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_size = (screen_width, screen_height)

class GameOfLife:
    def __init__(self, complexity):
        self.complexity = complexity               #Выбираем сложность и узнаём с установкой размер окна пользователя
        self.screen = pygame.display.set_mode(screen_size)

    def screen(self):
        pass

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('')
        back_ground_img = pygame.image.load('kosmos-art-hellsescapeartist-tylercreatesworlds.jpg')
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            #тестим правильную работу программы
            self.screen.blit(back_ground_img, (0, 0))
        pygame.quit()

if __name__ == '__main__':
    game = GameOfLife(3)
    game.run()
