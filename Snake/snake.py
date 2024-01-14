import pygame as pg
from game_objects import Grid
from game_objects import Screen
from snake_objects import Snake
from random import randint

WIDTH = 600
HEIGHT = 600

# game setup
def setup():
    global screen, grid, snake, food, time, time_steps
    screen = Screen(WIDTH, HEIGHT)
    grid = Grid(rows=20, cols=20, cell_size=30)
    snake = Snake(randint(0, grid.rows-1), randint(0, grid.cols-1))
    food = Snake.Food(randint(0, grid.rows-1), randint(0, grid.cols-1))
    time, time_steps = 0, 110

setup()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
    # Get user wasd and arrow key input
    keys = pg.key.get_pressed()
    only_head = len(snake()) == 1

    if (keys[pg.K_w] or keys[pg.K_UP]) and (snake()[0].direction != (1,0) or only_head):
        snake()[0].direction = (-1,0)
    elif ((keys[pg.K_s] or keys[pg.K_DOWN]) and (snake()[0].direction != (-1,0) or only_head)):
        snake()[0].direction = (1,0)
    elif ((keys[pg.K_a] or keys[pg.K_LEFT]) and (snake()[0].direction != (0,1) or only_head)):
        snake()[0].direction = (0,-1)
    elif ((keys[pg.K_d] or keys[pg.K_RIGHT]) and (snake()[0].direction != (0,-1) or only_head)):
        snake()[0].direction = (0,1)

    # Reset screen
    screen.set()

    # Update game objects
    time_now = pg.time.get_ticks()
    if time_now - time > time_steps:
        time = time_now
        snake.move(grid())
        snake.check_food(food, grid)

    if (snake.check_collision(grid)):
        setup()

    # Draw game objects
    snake.put(grid())
    food.put(grid())
    grid.draw(screen())

    # Flip() display to update screen
    screen.flip()

    # Limit FPS to 60
    screen.time_step(60)