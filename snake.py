from turtle import Turtle

START_POSITION = [(0,0), (-20,0), (-40,0)]
SNAKE_STEP = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITION:
            snake = Turtle('square')
            snake.color('white')
            snake.pu()
            snake.goto(position)
            self.segments.append(snake)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].fd(SNAKE_STEP)

