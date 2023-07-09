from turtle import Turtle, Screen

screen = Screen()
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self, ):
        self.snake = []
        self.positions = (20, 0, -20)
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.goto(self.positions[i], 0)
            self.snake.append(new_segment)

    def move_snake(self):
        for part in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part - 1].xcor()
            new_y = self.snake[part - 1].ycor()
            self.snake[part].goto(new_x, new_y)
        self.snake[0].forward(MOVE)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def grow(self):
        grow_segment = Turtle()
        screen.tracer(0)
        grow_segment.penup()
        grow_segment.shape("square")
        grow_segment.color("white")
        self.snake.append(grow_segment)
