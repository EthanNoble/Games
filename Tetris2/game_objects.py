import pygame as pg
from variables import colors as c
from variables import tetrominos
from random import choice
import numpy as np


class Tetromino: # Collection of block sprites, not a sprite itself
    def __init__(self, block_size, x, y, type=None, color=None, alpha=255, border_width=0):
        # Random tetromino color
        tetromino_colors = list(c.values())[:8]
        self.color = choice(tetromino_colors) if color is None else color

        # Create 4 blocks for tetromino
        self.block_size = block_size
        self.x = x
        self.y = y
        self.alpha = alpha
        blocks = [FallingBlock(block_size, x, y, self.color, alpha, border_width) for _ in range(4)]
        self.block_group = pg.sprite.RenderUpdates(blocks)

        # Select random tetromino type
        self.current_shape = 0 # On rotation, this will be incremented and applied modulo
        self.key = choice(list(tetrominos.keys())) if type is None else type
        self.shape = tetrominos[self.key][0] # Grab first unrotated tetromino

        # self.key = 'T'
        # self.shape = tetrominos[self.key][0]
        self.__position_blocks()
    
    def __position_blocks(self): # Position blocks according to tetromino type
        relative_positions = [] # Relative positions of blocks in tetromino
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                if self.shape[y][x] == 1:
                    relative_positions.append((x, y))

        # Add relative positions to the blocks absolute x and y positions
        for i, block in enumerate(self.block_group.sprites()):
            block.rect.x = self.x
            block.rect.y = self.y
            block.rect.x += relative_positions[i][0] * block.size
            block.rect.y += relative_positions[i][1] * block.size
        print()

    def update(self, floor_group, stable_tetrominos): # Check for collisions and update tetromino blocks
        # Check if tetromino collided with border or stable tetrominos
        if (not self.__collided_with_group(floor_group, y=-1) and
            not self.__collided_with_group(stable_tetrominos, y=-1)):
            self.y += self.block_size # Update vertical tetromino position
            self.block_group.update()
            return False
        return True # Tetromino collided with border, return True to indicate that it should be added to stable tetrominos

    def move_blocks_by(self, x, wall_group, stable_tetrominos): # Move all blocks horizontally in tetromino by x
        if (not self.__collided_with_group(wall_group, x=-1*x) and
            not self.__collided_with_group(stable_tetrominos, x=-1*x)):
            self.x += x * self.block_size # Update horizontal tetromino position
            for block in self.block_group.sprites():
                block.rect.x += x * block.size
    
    def rotate_blocks(self, wall_group, stable_tetrominos): # Rotate all blocks in tetromino
        pass
        # HARD CODED ROTATION METHOD
        all_rotated_shapes = tetrominos[self.key]
        self.current_shape += 1
        self.shape = all_rotated_shapes[self.current_shape % len(all_rotated_shapes)]
        self.__position_blocks()

        # If rotated tetromino collides with wall or stable tetrominos, rotate back
        if (self.__collided_with_group(wall_group) or
            self.__collided_with_group(stable_tetrominos)):
            # Reverse what we just did
            self.current_shape -= 1
            self.shape = all_rotated_shapes[self.current_shape % len(all_rotated_shapes)] # Revert to previous shape
            self.__position_blocks()

    
        # MATRIX ROTATION METHOD
        # relative_positions = np.array(self.shape)

        # # Rotate relative positions (transpose and flip horizontally)
        # rotated_relative_positions = relative_positions.T
        # rotated_relative_positions = np.fliplr(rotated_relative_positions)
        # self.shape = rotated_relative_positions.tolist()
        # self.__position_blocks()

        # # If rotated tetromino collides with wall or stable tetrominos, rotate back
        # if (self.__collided_with_group(wall_group) or
        #     self.__collided_with_group(stable_tetrominos)):
        #     # Reverse what we just did
        #     rotated_relative_positions = np.fliplr(rotated_relative_positions)
        #     rotated_relative_positions = rotated_relative_positions.T
        #     self.shape = rotated_relative_positions.tolist()
        #     self.__position_blocks()

    def __collided_with_group(self, group, x=0, y=0):
        # Hacky way to get collision detection to work
        self.block_group.update(direction_x=-1*x, direction_y=-1*y) # Move to check for collision
        collided = len(pg.sprite.groupcollide(self.block_group, group, False, False)) > 0
        self.block_group.update(direction_x=x, direction_y=y) # Move back to original position

        return collided


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

    def update(self, direction_x=0, direction_y=1):
        self.rect.x += direction_x*self.size
        self.rect.y += direction_y*self.size
