import pygame.sprite


class Player(pygame.sprite.Sprite):

    def __init__(self, size, column, row):
        super().__init__()
