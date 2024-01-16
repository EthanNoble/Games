import pygame as pg
from game_objects import StableBlock
from game_objects import Tetromino
from variables import colors as c


## TODO:
# 1. Separate border blocks into separate ceiling, floor, and wall groups each with distinct collision behavior
# 2. Figure out how to use collision detection with one step in the future


WIDTH = 650
HEIGHT = 660
GRID_WIDTH = 12
GRID_HEIGHT = 22
CELL_SIZE = 30


def borders():
    group = pg.sprite.RenderUpdates()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if (x is not 0 and
                x is not GRID_WIDTH-1 and
                y is not 0 and
                y is not GRID_HEIGHT-1):
                continue # Skip if not edge of grid
            block = StableBlock(CELL_SIZE, x*CELL_SIZE, y*CELL_SIZE, c['grey'])
            group.add(block)
    return group


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.SCALED)
    pg.display.set_caption('Tetris')
    pg.mouse.set_visible(True)

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((c['black']))

    screen.blit(background, (0, 0))
    pg.display.flip()

    # Game objects including sprites and groups
    border_group = borders()
    falling_x = (GRID_WIDTH//2) * CELL_SIZE
    falling_y = 1 * CELL_SIZE
    falling_tetromino = Tetromino(CELL_SIZE, falling_x, falling_y)
    # ghost_tetromino = Tetromino(CELL_SIZE, falling_x, falling_y, alpha=50)
    stable_tetrominos = pg.sprite.RenderUpdates()
    clock = pg.time.Clock()
    time, time_steps = 0, 350 # Controls tetromino drop speed

    running = True
    while running:
        clock.tick(60)

        # Input queue
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                falling_tetromino.move_blocks_by(-1)
            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                falling_tetromino.move_blocks_by(1)
            elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
                print('up')
            elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                print('down')
        
        # UPDATE ALL SPRITES HERE
        time_now = pg.time.get_ticks()
        if time_now - time > time_steps:
            time = time_now
            if falling_tetromino.update(border_group, stable_tetrominos):
                # If we get here, the falling tetromino collided with the border
                # and we add falling tetromino to stable tetrominos and create new
                # falling tetromino
                stable_tetrominos.add(falling_tetromino.block_group)
                falling_tetromino = Tetromino(CELL_SIZE, falling_x, falling_y)

        border_group.update()
                
        screen.blit(background, (0, 0))
        border_group.draw(screen)
        falling_tetromino.block_group.draw(screen)
        # ghost_tetromino.block_group.draw(screen)
        stable_tetrominos.draw(screen)

        pg.display.flip()
    
    pg.quit()


if __name__ == '__main__':
    main()
