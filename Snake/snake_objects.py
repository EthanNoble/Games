from random import randint

class Snake:
    def __init__(self, row, col):
        self.head = self.BodyPart(row, col)
        self.body = [self.head]


    def __call__(self):
        return self.body
    

    def put(self, grid):
        for body_part in self.body:
            body_part.put(grid)
    

    def move(self, grid):
        for body_part in reversed(self.body):
            body_part.move(grid)

            index = self.body.index(body_part)
            if (index > 0):
                body_part.direction = self.body[index-1].direction


    def check_collision(self, grid):
        # Check if snake collides with itself
        for body_part in self.body[1:]:
            if self.head.coords == body_part.coords:
                return True
        
        # Check if snake collides with wall
        if self.head.coords[0] < 0 or self.head.coords[0] >= grid.rows:
            return True
        elif self.head.coords[1] < 0 or self.head.coords[1] >= grid.cols:
            return True


    def add_body_part(self):
        self.body.append(self.BodyPart(
            self.body[-1].coords[0] - self.body[-1].direction[0],
            self.body[-1].coords[1] - self.body[-1].direction[1],
            self.body[-1].direction))

    def check_food(self, food, grid):
        if self.head.coords == food.coords:
            food.coords = (randint(0, grid.rows-1), randint(0, grid.cols-1))
            self.add_body_part()


    class BodyPart:
        def __init__(self, row, col, direction=(0,0)):
            self.coords = (row, col)
            self.direction = direction
        
        
        def put(self, grid):
            grid[self.coords[0]][self.coords[1]] = 3
        

        def move(self, grid):
            # Reset current position and move to new position
            grid[self.coords[0]][self.coords[1]] = 0
            self.coords = (self.coords[0] + self.direction[0], self.coords[1] + self.direction[1])


    class Food:
        def __init__(self, row, col):
            self.coords = (row, col)
        
        def put(self, grid):
            grid[self.coords[0]][self.coords[1]] = 4
