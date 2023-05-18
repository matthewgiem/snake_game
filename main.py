from turtle import Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()

game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()
    snake.move()

    screen.listen()
    screen.onkey(key="Up", fun=snake.snake_up)
    screen.onkey(key="Down", fun=snake.snake_down)
    screen.onkey(key="Left", fun=snake.snake_left)
    screen.onkey(key="Right", fun=snake.snake_right)


screen.exitonclick()
