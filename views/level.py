import pygame.sprite

from sprites.blocks import Wall, Background


class Level:
    SYMBOL_BACKGROUND = ' '
    SYMBOL_SPRITE = {SYMBOL_BACKGROUND: Background, '#': Wall}
    SIZE_BLOCK = 64

    def __init__(self, screen, config_file='config_level/default_level'):
        self.screen = screen
        self.size_matrix = (0, 0)
        self.all_sprites = pygame.sprite.Group()
        self.build_level(config_file=config_file)
        self.draw()

    def draw(self):
        self.all_sprites.draw(self.screen)

    def build_level(self, config_file) -> None:
        config_matrix: list[list[str]] = Level.read_config(config_file)
        self.size_matrix = (len(config_matrix[0]), len(config_matrix))
        self.level_matrix: list[list[any]] = []
        for row in range(self.size_matrix[1]):
            self.level_matrix.append([])
            for column in range(self.size_matrix[0]):
                object = self.construct_block(config_matrix[row][column], column, row)
                self.level_matrix[row].append(object)

    def construct_block(self, symbol: str, column: int, row: int) -> any:
        cls_block = Level.SYMBOL_SPRITE[symbol]
        block = cls_block(Level.SIZE_BLOCK, column, row, groups=(self.all_sprites))
        return block

    @staticmethod
    def read_config(path: str) -> list[list[str]]:
        config_matrix = []
        with open(path) as file:
            line = [symbol for symbol in file.readline()]
            line = [symbol if symbol in Level.SYMBOL_SPRITE else Level.SYMBOL_BACKGROUND for symbol in line]
            config_matrix.append(line)
        return config_matrix
