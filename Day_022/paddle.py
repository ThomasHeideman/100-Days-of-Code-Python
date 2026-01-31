from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        current_y = self.ycor() +  50
        self.goto(self.xcor(), current_y)

    def down(self):
        current_y = self.ycor() -  50
        self.goto(self.xcor(), current_y)


