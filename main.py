import pygame
from pygame.locals import *

from player import Player
from game import Game

SCREEN_WIDTH = 1060
SCREEN_HEIGHT = 547
clock = pygame.time.Clock()


class Button:
    def __init__(self, text, position):
        self.font = pygame.font.Font(None, 36)
        self.color = pygame.Color("white")
        self.text = self.font.render(text, True, self.color)
        self.rect = self.text.get_rect(center=position)

    def draw(self, surface):
        surface.blit(self.text, self.rect)


def main_menu():
    pygame.init()
    DISPLAY = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(DISPLAY)
    bg = pygame.image.load("resources/images/forest.jpg")
    pygame.display.set_caption("Игра")

    play_button = Button("Играть", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    exit_button = Button("Выйти из игры", (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 50))

    active_sprite_list = pygame.sprite.Group()
    player = Player(SCREEN_HEIGHT)
    active_sprite_list.add(player)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit("QUIT")

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    game = Game(screen, SCREEN_HEIGHT, SCREEN_WIDTH)
                    game.run()
                elif exit_button.rect.collidepoint(event.pos):
                    raise SystemExit("QUIT")

        screen.blit(bg, (0, 0))
        play_button.draw(screen)
        exit_button.draw(screen)
        # active_sprite_list.draw(screen)

        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    main_menu()