from main import *


class button:

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.active_clr = (120, 219, 226)
        self.inactive_clr = (70, 68, 81)

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.heigth:
                pygame.draw.rect(screen, self.active_clr, (x, y, self.width, self.heigth))
                if click[0] == 1 and action is not None:
                    action()
        else:
            pygame.draw.rect(screen, self.inactive_clr, (x, y, self.width, self.heigth))
        print_text(message, x + 10, y + 10)


def print_text(message, x, y, type=None):
    font = pygame.font.Font(type, 75)
    text = font.render(message, False, (255, 255, 255))
    screen.blit(text, (x, y))



