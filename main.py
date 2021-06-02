from snake import Snake
from food import Food
from scoreboard import Score
from turtle import Screen
import time

# setup screen and turn off tracer so we can control when screen is refreshed
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('PySnake')
screen.tracer(0)

# initialize classes
snake = Snake()
food = Food()
score = Score()

# listen for directional button clicks
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# variable to control the game loop
game_is_on = True

# start game loop
while game_is_on == True: 
    # update screen every 0.1 seconds
    screen.update()
    time.sleep(0.1)

    # start the snake in motion
    snake.move()

    # if snake eats a piece of food, refresh food, +1 to score, and grow snake
    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh()
        snake.grow()

    # if snake exits the game screen call game over and end game loop
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_is_on = False

    # check the segments of the snake to make sure that the head is never occupying the same space as one of them
    # but make sure to exclude the head itself
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

# keep screen open until clicked
screen.exitonclick()