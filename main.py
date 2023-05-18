from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

snake = []

for x in starting_position:
    segment = Turtle(shape="square")
    segment.penup()
    segment.color("white")
    segment.setpos(x)
    snake.append(segment)


def snake_up():
    snake[0].setheading(90)


def snake_left():
    snake[0].setheading(180)


def snake_right():
    snake[0].setheading(0)


def snake_down():
    snake[0].setheading(270)


game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()
    for segment_number in range(len(snake) - 1, 0, -1):
        new_x = snake[segment_number - 1].xcor()
        new_y = snake[segment_number - 1].ycor()
        snake[segment_number].goto(new_x, new_y)
    screen.listen()
    screen.onkey(key="Up", fun=snake_up)
    screen.onkey(key="Down", fun=snake_down)
    screen.onkey(key="Left", fun=snake_left)
    screen.onkey(key="Right", fun=snake_right)
    snake[0].forward(20)

screen.exitonclick()
