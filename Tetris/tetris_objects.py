from variables import colors
from random import randint
import pygame as pg

class TetrisBoard:
    def __init__(self):
        self.falling_tetromino = None
        self.new_tetromino()

        self.stable_tetrominos = []
    
    def new_tetromino(self):
        self.falling_tetromino = Tetromino(['cyan', 'orange', 'light green', 'pink', 'yellow'], 4, 5)
    
    def maneuver_falling_tetromino(self, grid, direction):
        if self.can_manuever_tetromino(grid, direction):
            if direction == 'left':
                self.clear_tetromino(grid)
                self.falling_tetromino.col -= 1
            if direction == 'right':
                self.clear_tetromino(grid)
                self.falling_tetromino.col += 1
    
    def can_manuever_tetromino(self, grid, direction):
        # Check collision with walls
        for coord in self.falling_tetromino.coordinates:
            if ((coord[0] + self.falling_tetromino.col <= 1 and direction == 'left') or
                (coord[1] + self.falling_tetromino.col >= len(grid[0])-2 and direction == 'right')):
                print(coord[0] + self.falling_tetromino.col, '', coord[1] + self.falling_tetromino.col)
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

    def drop_falling_tetromino(self, grid):
        if (self.can_drop_tetromino(grid)):
            # Set current tetromino blocks to black
            self.clear_tetromino(grid)
            
            # Move tetromino down
            self.falling_tetromino.row += 1
        else:
            # Here, tetromino has collided with floor or stable tetromino
            # Add tetromino to stable tetrominos
            self.stable_tetrominos.append(self.falling_tetromino)
            self.new_tetromino()
        
    def can_drop_tetromino(self, grid):
        # Check collision with top of stable tetrominos
        for falling_coord in self.falling_tetromino.coordinates:
            for stable_tetromino in self.stable_tetrominos:
                for stable_coord in stable_tetromino.coordinates:
                    if (falling_coord[0] + self.falling_tetromino.row+1 == stable_coord[0] + stable_tetromino.row and
                        falling_coord[1] + self.falling_tetromino.col == stable_coord[1] + stable_tetromino.col):
                        return False
                

        # Check collision with floor and ceiling
        for coord in self.falling_tetromino.coordinates:
            if (coord[0] + self.falling_tetromino.row <= 0 or
                coord[0] + self.falling_tetromino.row >= len(grid)-2):
                return False
        
        return True
            

    def clear_tetromino(self, grid): # Clears tetromino from grid for animation
        for coord in self.falling_tetromino.coordinates:
                grid[coord[0] + self.falling_tetromino.row][coord[1] + self.falling_tetromino.col] = colors['black']

class Tetromino:
    shapes = [
        [(0,0),(0,1),(0,2),(1,1)],  # T
        [(0,0),(1,0),(2,0),(2,1)],  # L
        [(0,0),(0,1),(1,1),(1,2)],  # Skew
        [(0,1),(1,1),(0,0),(1,0)],  # Square
        [(0,3),(0,2),(0,1),(0,0)]   # Straight
    ]

    def __init__(self, color, row, col, shape='random'):
        self.color = colors[color[randint(0, len(color)-1)]] # Random color
        self.row = row
        self.col = col

        if shape == 'random':
            self.coordinates = self.shapes[randint(0, len(self.shapes)-1)]
        else:
            self.coordinates = self.shapes[shape]

    def put(self, grid, screen):
        for coord in self.coordinates:
            grid[coord[0] + self.row][coord[1] + self.col] = self.color

            # For debugging
            pg.font.init()
            font = pg.font.SysFont('Comic Sans MS', 10)
            text = font.render(str(coord[0])+', '+str(coord[1]), False, colors['white'])
            screen().blit(text, (450+(coord[1]*50),100+(coord[0]*50)))
        
        
        