import sys
import pygame
from pygame import *
import tkinter as tk
from tkinter import *
from Logick import *
root = tk.Tk()

screen_width = root.winfo_screenwidth()             # | Узнаём высоту и ширину экрана пользователя
screen_height = root.winfo_screenheight()           # |

screen_size = (screen_width, screen_height)

pygame.init()
pygame.font.init()
pygame.display.init()
pygame.mixer.pre_init(44100, 32, 2, 4096)
pygame.mixer.init()
screen = pygame.display.set_mode(screen_size)
# teacher_1 = Colliding()                           # Не могу реализовать класс Colliding для проверки вхождения игрока в зону вхождения


class Game:

    def __init__(self, x, y):
        # self.screen = pygame.display.set_mode(screen_size)      # установка размера окна пользователя, сделал переменную @screen глобальной в начале кода, чтобы был удобный доступ
        self.x = x
        self.y = y
        self.speed = 10

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

        volume = 1
        show = True
        while show:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # show = False              # Смотри комментарий в цикле @ while running
                    sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
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
        volume = 1

        while running:

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # running = False           # Можно неприсваивать @running = False, тк строчка sys.exit() выполняет всю работу и программа завершается без ошибок
                    sys.exit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
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

            pygame.display.update()
            back_ground_img = pygame.image.load('background.jpg')  # Ставим задний фон
            screen.blit(back_ground_img, (0, 0))
            #teacher_1.teacher_movement(self)
            self.movement()     # Вызываем функцию движения персонажа (пока что просто зелёный шар)

        pygame.quit()

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

        # pygame.draw.rect(screen, pygame.Color("White"), (1000, 500, 50, 50))
        pygame.draw.circle(screen, pygame.Color("Green"), (int(self.x), int(self.y)), 30)



if __name__ == '__main__':
    game = Game(screen_width / 6, screen_height / 2)
    game.menu()


def start():
    game = Game(screen_width / 6, screen_height / 2)
    game.run()

