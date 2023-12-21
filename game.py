import pygame

from player import Player

from main import Menu

SCREEN_WIDTH = 1060
SCREEN_HEIGHT = 547
clock = pygame.time.Clock()


def game():
    pygame.init()
    DISPLAY = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(DISPLAY)
    bg = pygame.image.load("forest.jpg")
    pygame.display.set_caption("Игра")
    active_sprite_list = pygame.sprite.Group()
    player = Player()
    active_sprite_list.add(player)
    screen.blit(bg, (0, 0))
    clock = pygame.time.Clock()
    run = True
    menu = Menu()
    #кароч, тут ваще много чё можно добавить интересного, а ещё я не понимаю, чё оно не рисуется, трэш

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit("QUIT")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    menu.switch(-1)
                if event.key == pygame.K_s:
                    menu.switch(1)
                if event.key == pygame.K_e:
                    menu.select()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
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
        menu.draw(screen, 100, 100, 75)
        #active_sprite_list.draw(screen)
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
        if player.rect.left < 0:
            player.rect.left = 0

        clock.tick(30)
        pygame.display.update()
