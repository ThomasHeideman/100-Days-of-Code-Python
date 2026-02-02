STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("Dark Olive Green")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_forward(self):
        current_y = self.ycor() + MOVE_DISTANCE
        self.sety(current_y)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def reset_player(self):
        self.goto(STARTING_POSITION)

