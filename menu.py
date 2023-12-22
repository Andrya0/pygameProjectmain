import pygame.font
from pygame import draw

now_font = pygame.font.Font('arial', 50)


class Menu:
    def __init__(self):
        self.options = []
        self.callbacks = []
        self.now_option_index = 0

    def append_option(self, option, callback):
        self.options.append(now_font.render(option, True, (255, 255, 255)))
        self.callbacks.append(callback)

    def switch(self, direction):
        self.now_option_index = max(0, min(self.now_option_index + direction, len(self.options) - 1))

    def select(self):
        self.callbacks[self.now_option_index]()

    def draw(self, surface, x, y, indent):
        for i, option in enumerate(self.options):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * indent)
            if i == self.now_option_index:
                draw.rect(surface, (0, 100, 0), option_rect)
            surface.blit(option, option_rect)
