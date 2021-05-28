from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('PySnake')
screen.tracer(0)

snake = Snake()

while True: 
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()