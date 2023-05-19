from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
TIME_INCREMENT = 0.1


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.snake_up)
screen.onkey(key="Down", fun=snake.snake_down)
screen.onkey(key="Left", fun=snake.snake_left)
screen.onkey(key="Right", fun=snake.snake_right)

game_is_on = True
while game_is_on:
    time.sleep(TIME_INCREMENT)
    screen.update()
    snake.move()

# add food and change the time
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.eat_food()
        scoreboard.increase_score()
        # if TIME_INCREMENT > 0.3:
        #     TIME_INCREMENT -= .05
        # elif 0.3 >= TIME_INCREMENT >= 0.025:
        #     TIME_INCREMENT -= .025
        # elif TIME_INCREMENT == 0:
        #     game_is_on = False
        #     scoreboard.won()


# end the game if you go outside the map
    if snake.head.xcor() * snake.head.xcor() > 90000:
        game_is_on = False
        scoreboard.game_over()
    if snake.head.ycor() * snake.head.ycor() > 90000:
        game_is_on = False
        scoreboard.game_over()

# detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
