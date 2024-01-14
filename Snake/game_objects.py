import pygame as pg

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
    def __init__(self, rows, cols, cell_size, x_offset=0, y_offset=0):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.grid = [[0 for x in range(self.cols)] for y in range(self.rows)]

    def __call__(self):
        return self.grid
    
    def print_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.grid[row][col], end=' ')
            print()
    
    def get_cell_colors(self):
        return [
            (0, 0, 0), # black
            (255, 255, 255), # white
            (0, 0, 255), # blue
            (0, 255, 0), # green
            (255, 0, 0) # red
        ]
    
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                x = col*self.cell_size+self.x_offset
                y = row*self.cell_size+self.y_offset
                cell_rect = pg.Rect(x+1, y+1, self.cell_size-1, self.cell_size-1)
                pg.draw.rect(screen, self.get_cell_colors()[cell_value], cell_rect)