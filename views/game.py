import pygame
from views.level import Level


def run_game(size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    level = Level(screen)
    pygame.display.flip()

    clock = pygame.time.Clock()
    FPS = 60
    is_run = True

    while is_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False
        clock.tick(FPS)

    pygame.quit()
