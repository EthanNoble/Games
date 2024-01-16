from variables import colors
from random import randint
import pygame as pg

class TetrisBoard:
    def __init__(self):
        self.falling_tetromino = None
        self.new_tetromino()
        self.ghost_tetromino = None # For showing where tetromino will land

        self.stable_tetrominos = []
    
    def new_tetromino(self):
        self.falling_tetromino = Tetromino(['cyan', 'orange', 'light green', 'pink', 'yellow'], 4, 5)
    
    def rotate(self, grid):
        if (self.can_drop_tetromino(grid) and
            self.can_manuever_tetromino(grid, 'left') and
            self.can_manuever_tetromino(grid, 'right')):
            # Set current tetromino blocks to black
            self.clear_tetromino(grid)
            self.clear_tetromino(grid, ghost=True)
            self.falling_tetromino.shape_index += 5 if self.falling_tetromino.shape_index < 5 else -5
            self.falling_tetromino.coordinates = self.falling_tetromino.shapes[self.falling_tetromino.shape_index]
                


    def maneuver_falling_tetromino(self, grid, direction):
        if self.can_manuever_tetromino(grid, direction):
            if direction == 'left':
                self.clear_tetromino(grid)
                self.clear_tetromino(grid, ghost=True)
                self.falling_tetromino.col -= 1
            if direction == 'right':
                self.clear_tetromino(grid)
                self.clear_tetromino(grid, ghost=True)
                self.falling_tetromino.col += 1
    
    def can_manuever_tetromino(self, grid, direction):
        # Check collision with walls
        for coord in self.falling_tetromino.coordinates:
            if ((coord[0] + self.falling_tetromino.col <= 1 and direction == 'left') or
                (coord[1] + self.falling_tetromino.col >= len(grid[0])-2 and direction == 'right')):
                return False
        
        # Check collision with side of stable tetrominos
        for falling_coord in self.falling_tetromino.coordinates:
            for stable_tetromino in self.stable_tetrominos:
                for stable_coord in stable_tetromino.coordinates:
                    if (falling_coord[0] + self.falling_tetromino.row == stable_coord[0] + stable_tetromino.row and
                        falling_coord[1] + self.falling_tetromino.col+1 == stable_coord[1] + stable_tetromino.col and
                        direction == 'right'):
                        return False
                    elif (falling_coord[0] + self.falling_tetromino.row == stable_coord[0] + stable_tetromino.row and
                        falling_coord[1] + self.falling_tetromino.col-1 == stable_coord[1] + stable_tetromino.col and
                        direction == 'left'):
                        return False
        
        return True
    
    def generate_ghost_tetromino(self, grid):
        self.ghost_tetromino = Tetromino(['white'],
                                    self.falling_tetromino.row,
                                    self.falling_tetromino.col,
                                    shape=self.falling_tetromino.shape_index)
        while self.can_drop_tetromino(grid, ghost=True):
            self.drop_tetromino(grid, self.ghost_tetromino, ghost=True)
    
    def fully_drop(self, grid):
        while self.can_drop_tetromino(grid):
            self.drop_tetromino(grid, self.falling_tetromino)

    def drop_tetromino(self, grid, tetromino, ghost=False):
        if (self.can_drop_tetromino(grid)):
            # Set current tetromino blocks to black
            self.clear_tetromino(grid)
            
            # Move tetromino down
            tetromino.row += 1
        else:
            # Here, tetromino has collided with floor or stable tetromino
            # Add tetromino to stable tetrominos unless it is a ghost tetromino
            if not ghost:
                self.stable_tetrominos.append(tetromino)
                self.new_tetromino()
        
    def can_drop_tetromino(self, grid, ghost=False):
        if not ghost:
            # Check collision with top of stable tetrominos for falling tetromino
            for falling_coord in self.falling_tetromino.coordinates:
                for stable_tetromino in self.stable_tetrominos:
                    for stable_coord in stable_tetromino.coordinates:
                        if (falling_coord[0] + self.falling_tetromino.row+1 == stable_coord[0] + stable_tetromino.row and
                            falling_coord[1] + self.falling_tetromino.col == stable_coord[1] + stable_tetromino.col):
                            return False
            # Check collision with floor and ceiling for falling tetromino
            for coord in self.falling_tetromino.coordinates:
                if (coord[0] + self.falling_tetromino.row <= 0 or
                    coord[0] + self.falling_tetromino.row >= len(grid)-2):
                    return False
        else: # Is ghost tetromino
            # Check collision with top of stable tetrominos for ghost tetromino
            for ghost_coord in self.ghost_tetromino.coordinates:
                for stable_tetromino in self.stable_tetrominos:
                    for stable_coord in stable_tetromino.coordinates:
                        if (ghost_coord[0] + self.ghost_tetromino.row+1 == stable_coord[0] + stable_tetromino.row and
                            ghost_coord[1] + self.ghost_tetromino.col == stable_coord[1] + stable_tetromino.col):
                            return False
            # Check collision with floor and ceiling for ghost tetromino
            for coord in self.ghost_tetromino.coordinates:
                if (coord[0] + self.ghost_tetromino.row <= 0 or
                    coord[0] + self.ghost_tetromino.row >= len(grid)-2):
                    return False
        
        return True
            

    def clear_tetromino(self, grid, ghost=False): # Clears tetromino from grid for animation
        if not ghost:
            for coord in self.falling_tetromino.coordinates:
                    grid[coord[0] + self.falling_tetromino.row][coord[1] + self.falling_tetromino.col] = colors['black']
        else:
            for coord in self.ghost_tetromino.coordinates:
                    grid[coord[0] + self.ghost_tetromino.row][coord[1] + self.ghost_tetromino.col] = colors['black']

class Tetromino:
    shapes = [
        # NORMAL
        [(0,0),(0,1),(0,2),(1,1)],  # T
        [(0,0),(1,0),(2,0),(2,1)],  # L
        [(0,0),(0,1),(1,1),(1,2)],  # Skew
        [(0,1),(1,1),(0,0),(1,0)],  # Square
        [(0,3),(0,2),(0,1),(0,0)],  # Straight
        # ROTATED
        [(0,0),(1,0),(2,0),(1,1)],  # T
        [(0,0),(0,1),(0,2),(1,2)],  # L
        [(0,0),(1,0),(1,1),(2,1)],  # Skew
        [(1,0),(1,1),(0,0),(0,1)],  # Square
        [(3,0),(2,0),(1,0),(0,0)], # Straight
    ]

    def __init__(self, color, row, col, shape='random'):
        self.color = colors[color[randint(0, len(color)-1)]] # Random color
        self.row = row
        self.col = col

        self.shape_index = randint(0, len(self.shapes)-1)
        if shape == 'random':
            self.coordinates = self.shapes[self.shape_index]
        else:
            self.coordinates = self.shapes[shape]
            self.shape_index = shape

    def put(self, grid, screen):
        for coord in self.coordinates:
            grid[coord[0] + self.row][coord[1] + self.col] = self.color

            # For debugging (shows tetris coordinates in right side of screen)
            # pg.font.init()
            # font = pg.font.SysFont('Comic Sans MS', 10)
            # text = font.render(str(coord[0])+', '+str(coord[1]), False, colors['white'])
            # screen().blit(text, (450+(coord[1]*50),100+(coord[0]*50)))
        
        
        