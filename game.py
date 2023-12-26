import pygame

from player import Player

from menu import Menu


class Game:
    def __init__(self, screen, SCREEN_HEIGHT, SCREEN_WIDTH):
        self.screen = screen
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH

    def run(self):
        pygame.key.set_repeat(200, 70)
        bg = pygame.image.load("resources/images/forest.jpg")
        pygame.display.set_caption("Игра")

        active_sprite_list = pygame.sprite.Group()
        player = Player(self.SCREEN_HEIGHT)
        active_sprite_list.add(player)

        clock = pygame.time.Clock()

        running = True
        menu = Menu()
        menu.append_option("Quit", quit)
        # кароч, тут ваще много чё можно добавить интересного, а ещё я не понимаю, чё оно не рисуется, трэш

        while running:
            self.screen.blit(bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit("QUIT")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        menu.switch(-1)
                    if event.key == pygame.K_s:
                        menu.switch(1)
                    if event.key == pygame.K_RETURN:
                        menu.select()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_UP:
                        player.jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()

            active_sprite_list.update()
            menu.draw(self.screen, 100, 100, 75)
            active_sprite_list.draw(self.screen)

            if player.rect.right > self.SCREEN_WIDTH:
                player.rect.right = self.SCREEN_WIDTH

            if player.rect.left < 0:
                player.rect.left = 0

            clock.tick(30)
            pygame.display.update()
