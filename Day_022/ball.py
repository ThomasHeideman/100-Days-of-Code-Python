import random
from turtle import Turtle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor,y_cor)

    def bounce_wall(self):
        self.y_move *= - 1.05

    def bounce_paddle(self):
        self.x_move *= - 1.05


    def reset_ball(self):
        self.goto(0, 0)
        self.x_move *= -1


