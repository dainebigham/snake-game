from turtle import Turtle

# constants for snake directions, snake step, and the inital array for building the snake segments 
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

    # add a new segment at the position of the three element in the starting array
    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    # create a new segment and send it to the back of the snake
    def add_segment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.pu()
        segment.goto(position)
        self.segments.append(segment)

    # add a segment to the current snake segments array
    def grow(self):
        self.add_segment(self.segments[-1].position())

    # loop through snake segments from last to first, moving the final segment to the position of the second to last segment
    # and repeating until the entire body of the snake up to the head has moved forwards and/or changed direction
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.fd(SNAKE_STEP)

    # methods for changing the snakes direction
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

