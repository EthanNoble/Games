import pygame as pg
from game_objects import StableBlock
from game_objects import Tetromino
from variables import colors as c


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
    falling_x = (GRID_WIDTH//2 - 2) * CELL_SIZE
    falling_y = 1 * CELL_SIZE
    falling_tetromino = Tetromino(CELL_SIZE, falling_x, falling_y)
    clock = pg.time.Clock()
    time, time_steps = 0, 350 # Controls tetromino drop speed

    running = True
    while running:
        clock.tick(60)

        # Input queue
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        # UPDATE ALL SPRITES HERE
        time_now = pg.time.get_ticks()
        if time_now - time > time_steps:
            time = time_now
            falling_tetromino.block_group.update()
        border_group.update()
                
        screen.blit(background, (0, 0))
        # DRAW ALL SPRITES HERE
        border_group.draw(screen)
        falling_tetromino.block_group.draw(screen)

        pg.display.flip()
    
    pg.quit()


if __name__ == '__main__':
    main()
