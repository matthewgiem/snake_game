from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for x in STARTING_POSITION:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.setpos(x)
            self.snake.append(segment)

    def snake_up(self):
        self.snake[0].setheading(90)

    def snake_left(self):
        self.snake[0].setheading(180)

    def snake_right(self):
        self.snake[0].setheading(0)

    def snake_down(self):
        self.snake[0].setheading(270)

    def move(self):
        for segment_number in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment_number - 1].xcor()
            new_y = self.snake[segment_number - 1].ycor()
            self.snake[segment_number].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)
