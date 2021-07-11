from Logick import *
import sys
import pygame
from pygame import *
import tkinter as tk
from tkinter import *
import math

root = tk.Tk()

screen_width = root.winfo_screenwidth()             # Узнаём высоту и ширину экрана пользователя
screen_height = root.winfo_screenheight()

screen_size = (screen_width, screen_height)

pygame.init()
pygame.font.init()
pygame.display.init()
pygame.mixer.pre_init(44100, 32, 2, 4096)
pygame.mixer.init()
screen = pygame.display.set_mode(screen_size)


class Game:

    def __init__(self, x, y):
        # self.screen = pygame.display.set_mode(screen_size)      # установка размера окна пользователя, сделал переменную @screen глобальной в начале кода, чтобы был удобный доступ
        self.x = x
        self.y = y
        self.speed = 15

    global screen

    def usr_screen(self):
        pass

    def menu(self):

        pygame.display.set_caption('')

        menu_bckg = pygame.image.load('menu.jpg')

        music = 'menu_music.ogg'
        pygame.mixer.music.load(music)                  # Настройка микшера для проигрывания в меню, музыка ставится на паузу с помощью ПРОБЕЛА
        pygame.mixer.music.play(-1)
        pygame.mixer.Sound(music)
        pause = False

        start_btn = button(140, 70)
        quit_btn = button(140, 70)

        volume = 0.5
        show = True

        while show:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # show = False              # Смотри комментарий в цикле @ while running
                    sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_3:             # Ставить музыку на паузу "3"
                        pause = not pause
                        if pause:
                            pygame.mixer.music.pause()          # дописать чтобы в меню можно было убавить музыку
                        else:
                            pygame.mixer.music.unpause()
                    elif event.key == pygame.K_1:               # Убавление звука на "1"
                        volume -= 0.1
                        pygame.mixer.music.set_volume(volume)
                    elif event.key == pygame.K_2:               # Прибавление звука на "2"
                        volume += 0.1
                        pygame.mixer.music.set_volume(volume)

            pygame.display.update()
            screen.blit(menu_bckg, (0, 0))

            start_btn.draw(1700, 500, "Start", start)          # Здесь реализованы кнопки начала игры и выхода
            quit_btn.draw(1700, 600, "Quit", sys.exit)

    def run(self):

        clock = pygame.time.Clock()
        pygame.display.set_caption('Выжить на сессии')
        running = True

        file = 'secret.ogg'
        pygame.mixer.music.load(file)                   # Настройка микшера для проигрывания, музыка ставится на паузу с помощью ПРОБЕЛА
        pygame.mixer.music.play(-1)
        pygame.mixer.Sound(file)
        flpause = False
        volume = 0.5

        coords = (1300, 400)
        speed = 10                      # Переменные для движения сраного чёрного шарика по кругу
        next_tick = 500
        angle = 0

        while running:

            clock.tick(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # running = False           # Можно неприсваивать @running = False, тк строчка sys.exit() выполняет всю работу и программа завершается без ошибок
                    sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_3:             # Ставить музыку на паузу "3"
                        flpause = not flpause
                        if flpause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                    elif event.key == pygame.K_1:               # Убавление звука на "1"
                        volume -= 0.1
                        pygame.mixer.music.set_volume(volume)
                    elif event.key == pygame.K_2:               # Прибавление звука на "2"
                        volume += 0.1
                        pygame.mixer.music.set_volume(volume)

            ticks = pygame.time.get_ticks()
            if ticks > next_tick:
                next_tick += speed
                angle += 1                                                                                      # Хрень для движения сраного чёрного шарика по кругу
                coords = move_coords(angle, 2, coords)
            teacher = pygame.draw.rect(screen, pygame.Color("Black"), (coords[0], coords[1], 60, 60))

            pygame.display.update()
            back_ground_img = pygame.image.load('background.jpg')           # Ставим задний фон
            screen.blit(back_ground_img, (0, 0))
            self.movement()                                         # Вызываем функцию движения персонажа (пока что просто зелёный квадрат)
            if player.collidepoint(teacher.center):
                teacher_1.collide()

    def movement(self):                 # Здесь прописано движение персонажа игрока с его прорисовкой

        global usr_x, usr_y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.x < 1880:
            self.x += self.speed
            usr_x = self.x
        if keys[pygame.K_a] and self.x > 50:
            self.x -= self.speed
            usr_x = self.x
        if keys[pygame.K_w] and self.y > 50:
            self.y -= self.speed
            usr_y = self.y
        if keys[pygame.K_s] and self.y < 990:
            self.y += self.speed
            usr_y = self.y
        global player
        player = pygame.draw.rect(screen, pygame.Color("Green"), (int(self.x), int(self.y), 60, 60))


class Colliding:

    def __init__(self):
        self.x = 1000
        self.y = 500
        self.speed = 30

    def collide(self):                          # В этой функции мы ставим на паузу игру и вызываем окно tkinter с вопросами для пользователя (в случае если игрок в зоне препода)
        game_pause = True
        while game_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            pygame.draw.circle(screen, pygame.Color("Red"), (500, 500), 30)


teacher_1 = Colliding()


if __name__ == '__main__':
    game = Game(screen_width / 6, screen_height / 2)
    game.menu()


def start():
    game = Game(screen_width / 6, screen_height / 2)
    game.run()


def move_coords(angle, radius, coords):             # Ещё хрень для движения сраного чёрного шарика
    theta = math.radians(angle)
    return coords[0] + radius * math.cos(theta), coords[1] + radius * math.sin(theta)
