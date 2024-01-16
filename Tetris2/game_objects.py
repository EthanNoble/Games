import pygame as pg
from variables import colors as c
from variables import tetrominos
from random import choice


class Tetromino: # Collection of block sprites, not a sprite itself
    def __init__(self, block_size, x, y, alpha=255, border_width=0):
        # Random tetromino color
        tetromino_colors = [c['cyan'], c['orange'], c['light green'], c['yellow'], c['pink']]
        color = choice(tetromino_colors)

        # Create 4 blocks for tetromino
        blocks = [FallingBlock(block_size, x, y, color, alpha, border_width) for _ in range(4)]
        self.block_group = pg.sprite.RenderUpdates(blocks)

        # Select random tetromino type
        self.__type = choice(list(tetrominos.values()))
        self.__position_blocks()
    
    def __position_blocks(self): # Position blocks according to tetromino type
        relative_positions = [] # Relative positions of blocks in tetromino
        for y in range(len(self.__type)):
            for x in range(len(self.__type[y])):
                if self.__type[y][x] is 1:
                    relative_positions.append((x, y))

        # Add relative positions to the blocks absolute x and y positions
        for i, block in enumerate(self.block_group.sprites()):
            block.rect.x += relative_positions[i][0] * block.size
            block.rect.y += relative_positions[i][1] * block.size

    def update(self, border_group, stable_tetrominos): # Check for collisions and update tetromino blocks
        # Check if tetromino collided with border or stable tetrominos
        if not self.__collided_with_border(border_group) and not self.__collided_with_tetrominos(stable_tetrominos):
            self.block_group.update()
            return False
        return True # Tetromino collided with border, return True to indicate that it should be added to stable tetrominos

    def move_blocks_by(self, x): # Move all blocks in tetromino by x
        for block in self.block_group.sprites():
            block.rect.x += x * block.size
    
    def __collided_with_border(self, border_group):
        return len(pg.sprite.groupcollide(self.block_group, border_group, False, False)) > 0
    
    def __collided_with_tetrominos(self, stable_tetrominos):
        return len(pg.sprite.groupcollide(self.block_group, stable_tetrominos, False, False)) > 0


class Block(pg.sprite.Sprite):
    def __init__(self, size, x, y, color, alpha=255, border_width=0): # border_width = 0 -> no border & filled block
        pg.sprite.Sprite.__init__(self)

        self.size = size
        self.image = pg.Surface([size, size])
        self.image.set_alpha(alpha)
        self.image.fill(color)

        # Set the values of rect.x and rect.y to update block's position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class StableBlock(Block):
    def __init__(self, size, x, y, color, alpha=255, border_width=0):
        Block.__init__(self, size, x, y, color, alpha, border_width)

    def update(self):
        pass

class FallingBlock(Block):
    def __init__(self, size, x, y, color, alpha=255, border_width=0):
        Block.__init__(self, size, x, y, color, alpha, border_width)
        # self.rect.height += 1 # Make block 1 pixel taller downwards to allow for proper collision detection

    def update(self):
        self.rect.y += self.size