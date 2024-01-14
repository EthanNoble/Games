import pygame as pg
from game_objects import Grid
from game_objects import Screen
from tetris_objects import Tetromino
from tetris_objects import TetrisBoard
from random import randint
from variables import colors

WIDTH = 650
HEIGHT = 660

# game setup
def setup():
    global tetris_board, screen, grid, time, time_steps, move_time, move_time_steps

    grid_rows = 22
    grid_cols = 12

    #Tetris objects
    tetris_board = TetrisBoard()
    tetris_grid = []
    for row in range(grid_rows):
        tetris_grid.append([])
        for col in range(grid_cols):
            if (col == 0 or
                col == grid_cols-1 or
                row == 0 or
                row == grid_rows-1):
                tetris_grid[row].append(colors['grey'])
            else:
                tetris_grid[row].append(colors['black'])

    # Screen and grid setup
    screen = Screen(WIDTH, HEIGHT, color=colors['black'])
    grid = Grid(rows=grid_rows, cols=grid_cols, cell_size=30, custom_grid=tetris_grid)

    time, time_steps = 0, 350
    move_time, move_time_steps = 0, 200

setup()

move_left = False
move_right = False
rotate = False
fully_drop = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
    # Get user wasd and arrow key input
    keys = pg.key.get_pressed()

    if (keys[pg.K_w] or keys[pg.K_UP]): # Rotate tetromino
        rotate = True
    elif (keys[pg.K_s] or keys[pg.K_DOWN]): # Drop tetromino
        fully_drop = True
    elif (keys[pg.K_a] or keys[pg.K_LEFT]):
        move_left = True
    elif (keys[pg.K_d] or keys[pg.K_RIGHT]):
        move_right = True

    # Reset screen
    # screen.set()

    # Update game objects
    time_now = pg.time.get_ticks()
    if time_now - time > time_steps:
        time = time_now

        tetris_board.drop_tetromino(grid(), tetris_board.falling_tetromino)
    
    # Update move commands
    if time_now - move_time > move_time_steps:
        move_time = time_now
        if (rotate):
            tetris_board.rotate(grid())
            rotate = False
        if (fully_drop):
            tetris_board.fully_drop(grid())
            fully_drop = False
        if (move_left):
            tetris_board.maneuver_falling_tetromino(grid(), 'left')
            move_left = False
        if (move_right):
            tetris_board.maneuver_falling_tetromino(grid(), 'right')
            move_right = False

    # Draw game objects
    tetris_board.generate_ghost_tetromino(grid())
    tetris_board.ghost_tetromino.put(grid(), screen)
    tetris_board.falling_tetromino.put(grid(), screen)
    grid.draw(screen())

    # Flip() display to update screen
    screen.flip()
    # Clear text
    screen().fill(colors['black'])

    # Limit FPS to 60
    screen.time_step(60)