from turtle import Turtle

START_POSITION = [(0,0), (-20,0), (-40,0)]
SNAKE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.pu()
        segment.goto(position)
        self.segments.append(segment)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.fd(SNAKE_STEP)

    def up(self): 
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self): 
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self): 
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self): 
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

