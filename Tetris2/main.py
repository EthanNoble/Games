import pygame as pg
from game_objects import StableBlock
from game_objects import Tetromino
from variables import colors as c


# TODO:
# Make rotations work like it is in the real game


WIDTH = 650
HEIGHT = 659
GRID_WIDTH = 12
GRID_HEIGHT = 22
CELL_SIZE = 30

INSTANT_DROP = False


def borders():
    floor_border = pg.sprite.RenderUpdates()
    ceiling_border = pg.sprite.RenderUpdates()
    wall_border = pg.sprite.RenderUpdates()

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if y == GRID_HEIGHT-1: # Floor
                block = StableBlock(CELL_SIZE, x*CELL_SIZE, y*CELL_SIZE, c['grey'])
                floor_border.add(block)
            elif y == 0: # Ceiling
                block = StableBlock(CELL_SIZE, x*CELL_SIZE, y*CELL_SIZE, c['grey'])
                ceiling_border.add(block)
            elif x == 0 or x == GRID_WIDTH-1: # Walls
                block = StableBlock(CELL_SIZE, x*CELL_SIZE, y*CELL_SIZE, c['grey'])
                wall_border.add(block)

    return floor_border, ceiling_border, wall_border


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
    floor_group, ceiling_group, wall_group = borders()
    falling_x = (GRID_WIDTH//2) * CELL_SIZE
    falling_y = 1 * CELL_SIZE
    falling_tetromino = Tetromino(CELL_SIZE, falling_x, falling_y)
    stable_tetrominos = pg.sprite.RenderUpdates()
    clock = pg.time.Clock()
    time, time_steps = 0, 350 # Controls tetromino drop speed

    control, player_control_speed = 0, 4 # Controls player initiated left/right movement speed

    running = True
    while running:
        clock.tick(60)

        # Input management
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # Rotate tetromino
            if event.type == pg.KEYDOWN and (keys[pg.K_w] or keys[pg.K_UP]):
                falling_tetromino.rotate_blocks(wall_group, stable_tetrominos)
            # Player initiated instant drop
            elif INSTANT_DROP and (keys[pg.K_s] or keys[pg.K_DOWN]):
                while not falling_tetromino.update(floor_group, stable_tetrominos): pass

        # Player initiated gradual drop
        if not INSTANT_DROP and (event.type == pg.KEYDOWN and (keys[pg.K_s] or keys[pg.K_DOWN])):
            falling_tetromino.update(floor_group, stable_tetrominos)
        
        # Move left/right
        if control % player_control_speed == 0:
            if keys[pg.K_a] or keys[pg.K_LEFT]:
                falling_tetromino.move_blocks_by(-1, wall_group, stable_tetrominos)
            elif keys[pg.K_d] or keys[pg.K_RIGHT]:
                falling_tetromino.move_blocks_by(1, wall_group, stable_tetrominos)
        
        time_now = pg.time.get_ticks()
        if time_now - time > time_steps:
            time = time_now
            if falling_tetromino.update(floor_group, stable_tetrominos):
                # If we get here, the falling tetromino collided with the floor or
                # stable tetrominos and we add falling tetromino to stable tetrominos
                # and create new falling tetromino
                stable_tetrominos.add(falling_tetromino.block_group)
                falling_tetromino = Tetromino(CELL_SIZE, falling_x, falling_y)

        floor_group.update()
        ceiling_group.update()
        wall_group.update()
                
        screen.blit(background, (0, 0))
        floor_group.draw(screen)
        ceiling_group.draw(screen)
        wall_group.draw(screen)
        falling_tetromino.block_group.draw(screen)
        stable_tetrominos.draw(screen)

        pg.display.flip()

        control += 1
    
    pg.quit()


if __name__ == '__main__':
    main()
