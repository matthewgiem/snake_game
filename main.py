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

with open("high_score.txt") as file:
    contents = file.read()
    scoreboard.high_score = int(contents)
    scoreboard.update_scoreboard()


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


# end the game if you go outside the map
    if snake.head.xcor() * snake.head.xcor() > 90000:
        scoreboard.reset_scoreboard()
        time.sleep(2)
        print(f"score {scoreboard.score}, high score {scoreboard.high_score}")
        snake.reset_snake()
    if snake.head.ycor() * snake.head.ycor() > 90000:
        scoreboard.reset_scoreboard()
        time.sleep(2)
        print(f"score {scoreboard.score}, high score {scoreboard.high_score}")
        snake.reset_snake()

# detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset_scoreboard()
            print(f"score {scoreboard.score}, high score {scoreboard.high_score}")
            time.sleep(2)
            snake.reset_snake()

screen.exitonclick()
