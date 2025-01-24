import pygame.sprite
from pygame.examples.aliens import load_image


class Block(pygame.sprite.Sprite):
    def __init__(self, size_block: int, column: int, row: int, groups, path: str):
        super().__init__(*groups)
        self.size_block = size_block
        image = load_image(path)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.size_block * column
        self.rect.y = self.size_block * row


class Background(Block):
    def __init__(self, *args, **kwargs):
        kwargs['path'] = 'image/background.png'
        super().__init__(*args, **kwargs)


class Wall(Block):
    def __init__(self, *args, **kwargs):
        kwargs['path'] = 'image/wall.png'
        super().__init__(*args, **kwargs)
