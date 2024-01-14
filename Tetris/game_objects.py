import pygame as pg
from variables import colors

class Screen:
    def __init__(self, width, height, color=(100, 100, 100)):
        self.width = width
        self.height = height
        self.color = color
        self.screen = None
        self.clock = None
        self.dt = None
        self.init_screen()
    
    def __call__(self):
        return self.screen

    def init_screen(self):
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.dt = 0
    
    def set(self):
        self.screen.fill(self.color) # Reset screen
    
    def flip(self):
        pg.display.flip()

    def time_step(self, fps):
        self.dt = self.clock.tick(fps) / 1000


class Grid:
    def __init__(self, rows, cols, cell_size, x_offset=0, y_offset=0, custom_grid='default'):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.x_offset = x_offset
        self.y_offset = y_offset

        if custom_grid == 'default':
            self.grid = [[colors['black'] for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            self.grid = custom_grid

    def __call__(self):
        return self.grid
    
    def print_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end=' ')
            print()
    
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_color = self.grid[row][col]
                x = col*self.cell_size+self.x_offset
                y = row*self.cell_size+self.y_offset
                cell_rect = pg.Rect(x+1, y+1, self.cell_size-1, self.cell_size-1)
                if (cell_color == colors['white']): # For drawing ghost tetrominos
                    pg.draw.rect(screen, cell_color, cell_rect, 1)
                else:
                    pg.draw.rect(screen, cell_color, cell_rect)
